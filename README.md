# 📝 The Journal — Personal Blog

A minimal, elegant personal blog built with **Flask** and **JSON file storage** — no database setup required.

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install flask
```

### 2. Run the app
```bash
python app.py
```

### 3. Open in browser
```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
personal-blog/
├── app.py                  ← Flask routes + JSON file I/O
├── posts.json              ← Your posts database (auto-created)
├── requirements.txt
├── static/
│   └── style.css           ← Warm editorial aesthetic styles
└── templates/
    ├── base.html            ← Shared layout (header, footer)
    ├── index.html           ← Homepage with post list + tag filter
    ├── post.html            ← Single post reader
    ├── about.html           ← About page
    ├── admin.html           ← Admin dashboard (manage posts)
    ├── post_form.html       ← Create / edit post form
    └── login.html           ← Admin login page
```

---

## ✨ Features

- 📖 Clean public blog with featured first post
- 🏷️ Tag filtering on the homepage
- 📝 Draft / Publish toggle — write privately, go live when ready
- 🔒 Admin panel protected by login session
- 🔗 Auto slug generation from post title
- ✂️ Auto excerpt if left blank
- 💾 All data saved to `posts.json` — no database needed
- 🎨 Elegant editorial aesthetic with Cormorant Garamond + DM Sans fonts

---

## 🔐 Admin Access

The blog has a single admin account — only you can write and manage posts.

**Default credentials:**
```
Username: admin
Password: password123
```

> ⚠️ Change the password before deploying! Open `app.py` and update:
> ```python
> ADMIN_USER = "admin"
> ADMIN_PASS = "your_new_password"
> ```

### Admin Routes

| Route | What it does |
|---|---|
| `/admin/login` | Login page |
| `/admin` | Dashboard — all posts |
| `/admin/new` | Create a new post |
| `/admin/edit/<id>` | Edit a post |
| `/admin/delete/<id>` | Delete a post |
| `/admin/toggle/<id>` | Publish / unpublish a post |
| `/admin/logout` | Logout |

---

## 🗃️ How Data is Stored

All posts are stored in `posts.json` as a list of objects:

```json
[
    {
        "id": 1,
        "title": "Why I Started Writing Online",
        "slug": "why-i-started-writing-online",
        "content": "Full post content here...",
        "excerpt": "Short summary shown on homepage.",
        "tags": ["writing", "life"],
        "published": true,
        "created_at": "2026-05-20 10:00:00",
        "updated_at": "2026-05-20 10:00:00"
    }
]
```

---

## 🛠️ How the JSON I/O Works

```python
# Read all posts
def read_posts():
    with open("posts.json", "r") as f:
        return json.load(f)

# Write all posts back
def write_posts(posts):
    with open("posts.json", "w") as f:
        json.dump(posts, f, indent=4)
```

Every create, edit, or delete reads the file, modifies the list in memory, then writes it back.

---

## 🌐 Public Routes

| Route | What visitors see |
|---|---|
| `/` | Homepage — all published posts |
| `/post/<slug>` | Full post reader |
| `/about` | About page |

Visitors cannot access any admin routes — they are protected by a login session check.

---

## 📦 Dependencies

| Package | Purpose        |
|---------|----------------|
| Flask   | Web framework  |

---

## 🔮 Possible Enhancements

- [ ] Markdown support in post editor
- [ ] Search bar
- [ ] Comment section
- [ ] RSS feed
- [ ] Multi-author support with user roles
- [ ] Post view counter
