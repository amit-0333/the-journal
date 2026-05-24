from flask import Flask, render_template, request, redirect, url_for, flash, session
import json, os
from datetime import datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

DATA_FILE  = "posts.json"
ADMIN_USER = "admin"
ADMIN_PASS = "password123"   # change this!

# ─── JSON Helpers ─────────────────────────────────────────────────────────────

def read_posts():
    if not os.path.exists(DATA_FILE):
        write_posts([])
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_posts(posts):
    with open(DATA_FILE, "w") as f:
        json.dump(posts, f, indent=4)

def get_next_id(posts):
    return max((p["id"] for p in posts), default=0) + 1

def slugify(text):
    import re
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text

# ─── Auth ──────────────────────────────────────────────────────────────────────

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("logged_in"):
            flash("Please log in to access the admin panel.", "error")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

# ─── Public Routes ─────────────────────────────────────────────────────────────

@app.route("/")
def index():
    posts = read_posts()
    published = [p for p in posts if p.get("published")]
    tag_filter = request.args.get("tag", "")
    if tag_filter:
        published = [p for p in published if tag_filter in p.get("tags", [])]
    published.sort(key=lambda x: x["created_at"], reverse=True)

    all_tags = []
    for p in read_posts():
        if p.get("published"):
            all_tags.extend(p.get("tags", []))
    unique_tags = sorted(set(all_tags))

    return render_template("index.html", posts=published, tag_filter=tag_filter, tags=unique_tags)


@app.route("/post/<slug>")
def post(slug):
    posts = read_posts()
    p = next((p for p in posts if p["slug"] == slug and p.get("published")), None)
    if not p:
        flash("Post not found.", "error")
        return redirect(url_for("index"))
    return render_template("post.html", post=p)


@app.route("/about")
def about():
    return render_template("about.html")

# ─── Auth Routes ───────────────────────────────────────────────────────────────

@app.route("/admin/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == ADMIN_USER and request.form["password"] == ADMIN_PASS:
            session["logged_in"] = True
            return redirect(url_for("admin"))
        flash("Invalid credentials.", "error")
    return render_template("login.html")


@app.route("/admin/logout")
def logout():
    session.clear()
    flash("Logged out.", "success")
    return redirect(url_for("index"))

# ─── Admin Routes ──────────────────────────────────────────────────────────────

@app.route("/admin")
@login_required
def admin():
    posts = read_posts()
    posts.sort(key=lambda x: x["created_at"], reverse=True)
    return render_template("admin.html", posts=posts)


@app.route("/admin/new", methods=["GET", "POST"])
@login_required
def new_post():
    if request.method == "POST":
        title   = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        excerpt = request.form.get("excerpt", "").strip()
        tags    = [t.strip() for t in request.form.get("tags", "").split(",") if t.strip()]
        publish = request.form.get("published") == "on"

        if not title or not content:
            flash("Title and content are required.", "error")
            return redirect(url_for("new_post"))

        posts = read_posts()
        base_slug = slugify(title)
        slug = base_slug
        count = 1
        while any(p["slug"] == slug for p in posts):
            slug = f"{base_slug}-{count}"
            count += 1

        posts.append({
            "id":         get_next_id(posts),
            "title":      title,
            "slug":       slug,
            "content":    content,
            "excerpt":    excerpt or content[:160] + "…",
            "tags":       tags,
            "published":  publish,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })
        write_posts(posts)
        flash("Post created!", "success")
        return redirect(url_for("admin"))

    return render_template("post_form.html", post=None, action="new")


@app.route("/admin/edit/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    posts = read_posts()
    p = next((p for p in posts if p["id"] == post_id), None)
    if not p:
        flash("Post not found.", "error")
        return redirect(url_for("admin"))

    if request.method == "POST":
        p["title"]      = request.form.get("title", "").strip()
        p["content"]    = request.form.get("content", "").strip()
        p["excerpt"]    = request.form.get("excerpt", "").strip() or p["content"][:160] + "…"
        p["tags"]       = [t.strip() for t in request.form.get("tags", "").split(",") if t.strip()]
        p["published"]  = request.form.get("published") == "on"
        p["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_posts(posts)
        flash("Post updated!", "success")
        return redirect(url_for("admin"))

    return render_template("post_form.html", post=p, action="edit")


@app.route("/admin/delete/<int:post_id>")
@login_required
def delete_post(post_id):
    posts = read_posts()
    posts = [p for p in posts if p["id"] != post_id]
    write_posts(posts)
    flash("Post deleted.", "success")
    return redirect(url_for("admin"))


@app.route("/admin/toggle/<int:post_id>")
@login_required
def toggle_publish(post_id):
    posts = read_posts()
    p = next((p for p in posts if p["id"] == post_id), None)
    if p:
        p["published"] = not p.get("published", False)
        write_posts(posts)
        status = "published" if p["published"] else "unpublished"
        flash(f'Post {status}.', "success")
    return redirect(url_for("admin"))


if __name__ == "__main__":
    app.run(debug=True)
