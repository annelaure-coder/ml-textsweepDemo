# TextSweep Demo

A small Django app that shows [`textsweep`](https://test.pypi.org/project/textsweep/) in action: paste messy text, clean it for ML preprocessing, and keep a short history of runs.

`textsweep` is published on **TestPyPI**, so install it from that index (Django still comes from regular PyPI).

## Folder structure

```
package-work/
├── manage.py
├── requirements.txt
├── textsweep_demo/          # Django project (settings, root URLs)
└── cleaner/                 # App: views, models, templates, static files
    ├── services.py          # Thin wrapper around textsweep.clean_text
    ├── static/cleaner/      # Plain CSS + vanilla JS
    └── templates/cleaner/   # base.html plus home and history pages
```

- `/` — textarea form (works with a normal POST if JavaScript is off)
- `/history/` — last 20 cleanings
- `/api/clean/` — JSON API used by the page’s `fetch` submit
- `/admin/` — Django admin (`CleaningRecord` is registered)

## Setup

From this directory:

```powershell
py -3 -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt --extra-index-url https://test.pypi.org/simple/
python manage.py migrate
python manage.py runserver
```

On macOS or Linux, activate with `source venv/bin/activate` instead of `.\venv\Scripts\Activate.ps1`.

Open http://127.0.0.1:8000/

Optional admin user:

```powershell
python manage.py createsuperuser
```

Then visit http://127.0.0.1:8000/admin/

## Tests

```powershell
python manage.py test
```

## API

`POST /api/clean/` with JSON `{"text": "..."}` returns:

```json
{
  "original": "...",
  "cleaned": "...",
  "stats": {
    "char_count_before": 0,
    "char_count_after": 0,
    "word_count_before": 0,
    "word_count_after": 0
  }
}
```

A missing or empty `text` field returns HTTP 400 with an `error` message.
