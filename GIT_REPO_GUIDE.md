# TextSweep Demo - Git Repository Guide

## 🚀 HOW TO RUN THE PROJECT

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd textsweep-demo

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
.\venv\Scripts\Activate.ps1
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt --extra-index-url https://test.pypi.org/simple/

# 5. Run migrations
python manage.py migrate

# 6. Start the server
python manage.py runserver

# 7. Open browser
# Go to: http://127.0.0.1:8000/
```

Optional - Create admin user:
```bash
python manage.py createsuperuser
# Then visit: http://127.0.0.1:8000/admin/
```

Run tests:
```bash
python manage.py test
```

---

## 📦 WHAT TO INCLUDE IN THE REPOSITORY

### ✅ INCLUDE (Push These):

```
package-work/
├── cleaner/                    ✅ Django app (all files)
│   ├── migrations/             ✅ Include migrations
│   ├── static/                 ✅ CSS and JS files
│   ├── templates/              ✅ HTML templates
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── services.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── textsweep_demo/             ✅ Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .gitignore                  ✅ Git ignore file
├── manage.py                   ✅ Django management script
├── README.md                   ✅ Project documentation
├── requirements.txt            ✅ Dependencies
└── _probe_textsweep.py         ✅ Test script (optional but useful)
```

### ❌ EXCLUDE (Don't Push These):

```
❌ venv/                        (virtual environment - excluded by .gitignore)
❌ db.sqlite3                   (database - excluded by .gitignore)
❌ __pycache__/                 (Python cache - excluded by .gitignore)
❌ *.pyc                        (compiled Python - excluded by .gitignore)
❌ .vscode/                     (editor settings - excluded by .gitignore)
❌ mobile-forms-app/            (separate React Native project - move it out)
❌ view/                        (empty folder - not needed)
❌ REPOSITORY_STRUCTURE.md      (just for your reference)
❌ GIT_REPO_GUIDE.md            (just for your reference)
```

---

## 📂 WHAT YOU ACTUALLY NEED TO PUSH

Based on what's used in the Django project:

### Core Django Files:
- `manage.py`
- `requirements.txt`
- `README.md`
- `.gitignore`

### Django Project Config:
- `textsweep_demo/` (entire folder)

### Django App:
- `cleaner/` (entire folder including all subfolders)

### Optional but Useful:
- `_probe_textsweep.py` (shows how to use textsweep package)

---

## 🗑️ BEFORE PUSHING - CLEANUP

Do this first:

1. **Delete these folders** (not needed for the demo):
   - `view/` (it's empty)
   - `mobile-forms-app/` (move it to a separate location/repo)

2. **Keep these** (but they won't be pushed due to .gitignore):
   - `venv/` (stays on your computer, ignored by git)
   - `db.sqlite3` (stays on your computer, ignored by git)

---

## 📝 SUMMARY - FILES TO PUSH:

```
Your Repository Will Contain:
├── .gitignore
├── README.md
├── requirements.txt
├── manage.py
├── _probe_textsweep.py
├── cleaner/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   └── *.py files
└── textsweep_demo/
    └── *.py files
```

Total size: Small (~50-100 files, mostly code)

---

## 🎯 FINAL STEPS:

1. Delete `view/` folder (empty)
2. Move `mobile-forms-app/` somewhere else
3. Delete `REPOSITORY_STRUCTURE.md` and `GIT_REPO_GUIDE.md` (optional)
4. Initialize git: `git init`
5. Add files: `git add .`
6. Commit: `git commit -m "Initial commit: TextSweep Django demo"`
7. Push to GitHub/GitLab

The `.gitignore` will automatically exclude venv/, db.sqlite3, and __pycache__
