# FastAPI Blog

A small FastAPI + Jinja2 blog demo that renders posts on the homepage and exposes them as JSON via an API endpoint.

## Features

- Server-rendered pages using **Jinja2** (template inheritance via `templates/layout.html`)
- Static assets served from `/static` (CSS/images via `StaticFiles`)
- Simple JSON API for posts at `/api/posts`

## Live Endpoints

- `GET /` — HTML homepage showing the list of posts
- `GET /api/posts` — JSON response with the current in-memory posts

## Tech Stack

- **FastAPI** (web framework)
- **Jinja2** (server-side rendering)
- **Bootstrap** (styling in `templates/layout.html`)
- **Static Files** (served from the `static/` directory)

## Project Structure

- `main.py`
  - Creates the FastAPI app
  - Mounts static files: `app.mount("/static", ...)`
  - Configures templates: `Jinja2Templates(directory="templates")`
  - Defines routes: `/` and `/api/posts`
- `templates/`
  - `layout.html` — base layout (navbar, footer, theme toggle)
  - `home.html` — extends `layout.html` and renders posts
- `static/`
  - `css/main.css` — site styles
  - `js/utils.js` — helper JS (if needed)
  - `profile_pics/default.jpg` — default author avatar

## Setup

You’re using Python **3.13+**.

```bash
# (recommended) create/activate a virtual environment if your tooling doesn’t already do it
uv init project_name
cd project_name
uv add "fastapi[standard]" # install dependencies
```

## Run

```bash
uv run fastapi dev main.py # for development
```

Then open:
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/api/posts`

## Customization

### Edit posts
Posts are currently stored in-memory in `main.py` as the `posts` list:

- `author`
- `title`
- `content`
- `date_posted`

To change what appears on the homepage and in the API, update that list.

### Update templates
- Update global layout in: `templates/layout.html`
- Update homepage rendering in: `templates/home.html`

`home.html` uses template inheritance:

```jinja2
{% extends "layout.html" %}
{% block content %}
  ...
{% endblock content %}
```

### Update styling
Edit `static/css/main.css`.

## Notes

- Because posts are hard-coded in `main.py`, they reset whenever you restart the server.
- This repo is a lightweight demo 
