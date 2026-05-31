<div align="center">

```
████████╗██╗  ██╗███████╗     ██╗ ██████╗ ██╗   ██╗██████╗ ███╗   ██╗ █████╗ ██╗     
╚══██╔══╝██║  ██║██╔════╝     ██║██╔═══██╗██║   ██║██╔══██╗████╗  ██║██╔══██╗██║     
   ██║   ███████║█████╗       ██║██║   ██║██║   ██║██████╔╝██╔██╗ ██║███████║██║     
   ██║   ██╔══██║██╔══╝  ██   ██║██║   ██║██║   ██║██╔══██╗██║╚██╗██║██╔══██║██║     
   ██║   ██║  ██║███████╗╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
```

### 📝 The Journal — Personal Blog

> A minimal, elegant personal blog built with **Flask** and **JSON file storage** — no database setup required.

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask)
![JSON](https://img.shields.io/badge/Storage-JSON-lightgrey?style=for-the-badge)
![HTML](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS-orange?style=for-the-badge)
![Auth](https://img.shields.io/badge/Admin-Session%20Auth-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

</div>

---

## 📌 About

The Journal is a **full-stack personal blog** built entirely with Flask and file-based JSON storage.
No database setup, no complex config — just run and write.

Built to master:
- Full CRUD operations on blog posts
- Session-based admin authentication
- Draft/publish workflow for content management
- Auto slug & excerpt generation
- Server-side rendering with Jinja2 templates
- Storing & managing structured data with JSON

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📖 Public Blog | Clean homepage with featured first post |
| 🏷️ Tag Filtering | Filter posts by tags on the homepage |
| 📝 Draft / Publish | Write privately, go live when ready |
| 🔒 Admin Panel | Protected by login session — only you can manage posts |
| 🔗 Auto Slug | Slug auto-generated from post title |
| ✂️ Auto Excerpt | Excerpt auto-generated if left blank |
| 💾 JSON Storage | All data saved to `posts.json` — no database needed |
| 🎨 Editorial UI | Elegant aesthetic with Cormorant Garamond + DM Sans fonts |

---

## 🗂️ Project Structure

```bash
personal-blog/
│
├── 📄 app.py                   # Flask routes + JSON file I/O
├── 📄 posts.json               # Posts database (auto-created)
├── 📄 requirements.txt
│
├── 📂 static/
│   └── style.css               # Warm editorial aesthetic styles
│
├── 📂 templates/
│   ├── base.html               # Shared layout — header & footer
│   ├── index.html              # Homepage — post list + tag filter
│   ├── post.html               # Single post reader
│   ├── about.html              # About page
│   ├── admin.html              # Admin dashboard — manage posts
│   ├── post_form.html          # Create / edit post form
│   └── login.html              # Admin login page
│
└── 📄 README.md
```

---

## ⚙️ How to Run

```bash
# 1. Clone the repository
git clone https://github.com/amit-0333/personal-blog.git

# 2. Navigate into the folder
cd personal-blog

# 3. Install dependencies
pip install flask

# 4. Run the app
python app.py

# 5. Open in browser
# → http://127.0.0.1:5000
```

---

## 🌐 Public Routes

| Route | What Visitors See |
|-------|-------------------|
| `/` | Homepage — all published posts |
| `/post/<slug>` | Full post reader |
| `/about` | About page |

> Visitors cannot access any admin routes — all protected by session check.

---

## 🔐 Admin Routes

| Route | What It Does |
|-------|--------------|
| `/admin/login` | Login page |
| `/admin` | Dashboard — all posts |
| `/admin/new` | Create a new post |
| `/admin/edit/<id>` | Edit a post |
| `/admin/delete/<id>` | Delete a post |
| `/admin/toggle/<id>` | Publish / unpublish a post |
| `/admin/logout` | Logout |

**Default credentials:**

```
Username: admin
Password: password123
```

> ⚠️ Change before deploying! Open `app.py` and update:
> ```python
> ADMIN_USER = "admin"
> ADMIN_PASS = "your_new_password"
> ```

---

## 🗃️ Data Format

Every post is stored in `posts.json` as a JSON object:

```json
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
```

---

## 🧠 How It Works

```
User Action
     │
     ▼
Flask Route (app.py)
     │
     ▼
Read posts.json
     │
     ▼
Add / Edit / Delete / Toggle
     │
     ▼
Update Post List in Memory
     │
     ▼
Write Back to posts.json
     │
     ▼
Render Updated Page
```

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

---

## 🧩 My Approach

```
1. 📖 Plan the routes — public vs admin
2. 🔨 Build JSON read/write logic first
3. 🔒 Add session-based login protection
4. 🖥️ Design templates with Jinja2
5. ✅ Test all CRUD operations end to end
```

---

## 🎯 Learning Goals

- [x] Build a complete Flask web application
- [x] Implement full CRUD for blog posts
- [x] Use JSON as a lightweight database
- [x] Add session-based admin authentication
- [x] Auto-generate slugs and excerpts
- [x] Build draft/publish workflow
- [x] Design a clean, editorial frontend
- [ ] Add Markdown support in post editor
- [ ] Add search bar
- [ ] Add comment section
- [ ] Add RSS feed
- [ ] Deploy to a cloud platform

---

## 🔮 Future Improvements

- [ ] Markdown support in post editor
- [ ] Search bar for posts
- [ ] Comment section
- [ ] RSS feed
- [ ] Multi-author support with user roles
- [ ] Post view counter

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| 🐍 Python | Backend development |
| 🌶️ Flask | Web framework |
| 📄 JSON | Local data storage |
| 🎨 HTML / CSS | Frontend interface |
| 🔧 Git & GitHub | Version control |

---

## 👨‍💻 Author

**Amit Kumar**

[![GitHub](https://img.shields.io/badge/GitHub-amit--0333-181717?style=flat&logo=github)](https://github.com/amit-0333)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Amit%20Kumar-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/amit-kumar-a62a3640a/)
[![Kaggle](https://img.shields.io/badge/Kaggle-amitkumar038975-20BEFF?style=flat&logo=kaggle)](https://www.kaggle.com/amitkumar038975)

---

<div align="center">

> 📝 *Built to practice full-stack Flask development — clean, minimal, and fully functional.*

⭐ **Star this repo if you found it useful!**

</div>
