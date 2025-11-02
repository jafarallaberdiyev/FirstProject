# FirstProject — Django Backend

Short: A simple Django backend with items/dashboard and conversation apps, media uploads, and ready-to-extend REST API.

## Features
- Items CRUD (admin + forms)
- Media upload (`media/item_images/`)
- Auth (Django admin, login required for dashboard pages)
- (Optional) DRF endpoints for Items/Conversations

## Tech Stack
- Python 3.10+
- Django 5.x
- SQLite (dev), ready for Postgres in prod
- Templates (HTML), static & media handling

## Project Structure
├─ core/ # settings, urls, wsgi/asgi
├─ item/ # item app: models, views, templates
├─ dashboard/ # dashboard pages
├─ conversation/ # conversation app
├─ media/item_images/
├─ manage.py
