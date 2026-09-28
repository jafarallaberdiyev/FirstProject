# FirstProject — Django Marketplace Backend

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.x-092E20?logo=django&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

A Django backend with an items dashboard and a conversation (messaging) app: item CRUD with image uploads, threaded comments, and authentication.

## Features

- 📦 Items CRUD with categories (admin + forms)
- 🖼️ Image uploads (`media/item_images/`)
- 💬 Conversations between users about an item
- 🗨️ Comments with replies
- 🔐 Auth: login required for dashboard pages

## Tech stack

Python 3.10+ · Django 5.x · SQLite (dev) · HTML templates · Pillow

## Getting started

```bash
git clone https://github.com/jafarallaberdiyev/FirstProject.git
cd FirstProject

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

pip install -r requirements.txt
cp .env.example .env           # then set your own SECRET_KEY

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/. Add categories in the admin at `/admin/`, then create items from the dashboard.

## Project structure

```
firstproject/  # settings, root URLs, WSGI/ASGI
core/          # home page, signup/login forms
item/          # items, categories, comments
dashboard/     # the user's own items
conversation/  # messages between buyer and seller
media/         # uploaded images
```

## License

[MIT](LICENSE)
