# Repository Structure Analysis

## 📦 THE TEXTSWEEP PACKAGE (Published on TestPyPI)

**Location:** NOT in this folder structure  
**Status:** Already published to TestPyPI  
**Install from:** `pip install textsweep==0.1.0 --index-url https://test.pypi.org/simple/`

The actual `textsweep` package source code is NOT in `package-work`. 
You must have built and published it separately to TestPyPI already.

---

## 🌐 THE DEMO APP (Django Application)

**Location:** `c:\Users\user\Documents\Year 3\ML\Django\package-work`

This entire `package-work` folder is **ONE Django project** that demonstrates the `textsweep` package.

### Structure:
```
package-work/                          ← ROOT of Django project
├── manage.py                          ← Django management script
├── db.sqlite3                         ← Database
├── requirements.txt                   ← Dependencies (django, textsweep)
├── README.md                          ← Project documentation
├── .gitignore                         ← Git ignore file
│
├── textsweep_demo/                    ← Django PROJECT settings
│   ├── __init__.py
│   ├── settings.py                    ← Project configuration
│   ├── urls.py                        ← Root URL routing
│   ├── wsgi.py
│   └── asgi.py
│
├── cleaner/                           ← Django APP (main functionality)
│   ├── models.py                      ← CleaningRecord model
│   ├── views.py                       ← Views (home, history, api_clean)
│   ├── urls.py                        ← App URL patterns
│   ├── forms.py                       ← CleanTextForm
│   ├── services.py                    ← Uses textsweep.clean_text()
│   ├── admin.py                       ← Django admin config
│   ├── tests.py                       ← Unit tests
│   ├── templates/cleaner/             ← HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   └── history.html
│   └── static/cleaner/                ← CSS and JavaScript
│       ├── css/style.css
│       └── js/script.js
│
├── mobile-forms-app/                  ← SEPARATE React Native project (NOT related to textsweep)
└── venv/                              ← Python virtual environment
```

---

## 🎯 WHAT YOU HAVE:

### 1️⃣ The TextSweep Package (Source Code)
**WHERE IS IT?** Not in this folder! You must have it elsewhere or already published it.

To find it, search your computer for:
- A folder with `setup.py` or `pyproject.toml`
- A folder named just `textsweep` (not `textsweep_demo`)
- Files like `textsweep/__init__.py`, `textsweep/cleaner.py`, etc.

### 2️⃣ The Django Demo App
**WHERE IS IT?** `c:\Users\user\Documents\Year 3\ML\Django\package-work`

This is what you have here - a complete Django application that:
- Installs `textsweep` as a dependency
- Demonstrates its functionality
- Has a web interface
- Saves cleaning history

---

## 📂 FOR CREATING REPOSITORIES:

### Repository #1: The TextSweep Package
**YOU NEED TO FIND THIS!**

Typical structure would be:
```
textsweep/                     ← Package repository root
├── README.md
├── setup.py                   ← Or pyproject.toml
├── LICENSE
├── .gitignore
├── tests/
└── textsweep/                 ← The actual package
    ├── __init__.py
    ├── cleaner.py             ← clean_text() function
    └── other_modules.py
```

**Search for it with:**
```powershell
Get-ChildItem -Path "C:\Users\user\Documents" -Recurse -Filter "setup.py" -ErrorAction SilentlyContinue | Where-Object { $_.Directory.Name -eq "textsweep" }
```

### Repository #2: The Django Demo App
**LOCATION:** `c:\Users\user\Documents\Year 3\ML\Django\package-work`

**What to include in Git:**
```
✅ Include:
- All Django project files (manage.py, settings.py, etc.)
- cleaner/ app
- textsweep_demo/ project config
- requirements.txt
- README.md
- .gitignore
- templates/
- static/

❌ Exclude (already in .gitignore):
- venv/
- db.sqlite3
- __pycache__/
- .pyc files
- mobile-forms-app/ (separate React Native project, should be its own repo)
```

---

## 🔍 NEXT STEPS TO FIND THE PACKAGE:

Run these commands to find where your textsweep package source is:

```powershell
# Search for setup.py files
Get-ChildItem -Path "C:\Users\user\Documents" -Recurse -Filter "setup.py" -Depth 5 -ErrorAction SilentlyContinue

# Search for pyproject.toml files
Get-ChildItem -Path "C:\Users\user\Documents" -Recurse -Filter "pyproject.toml" -Depth 5 -ErrorAction SilentlyContinue

# Search for folders named textsweep (not textsweep_demo)
Get-ChildItem -Path "C:\Users\user\Documents" -Recurse -Directory -Filter "textsweep" -Depth 4 -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notlike "*textsweep_demo*" }
```

---

## 📝 SUMMARY:

| What | Where | Purpose |
|------|-------|---------|
| **TextSweep Package** | ❓ Unknown (need to find) | The actual Python package with clean_text() function |
| **Django Demo App** | `package-work/` | Web app that uses textsweep package |
| **React Native App** | `package-work/mobile-forms-app/` | Unrelated mobile forms demo |

You need TWO repositories:
1. **textsweep** (the package) - Need to locate this
2. **textsweep-demo** (the Django app) - This is `package-work/`
