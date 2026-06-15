# uv run main.py
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Glory Kinya",
        "title": "Regex and Algorithms",
        "content": "This series covers all regex patterns and an introduction to three common Algorithms: Binary Search, Selection Sort, and Quick Sort.",
        "date_posted": "June 13, 2026"
    }, 
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better!",
        "date_posted": "June 15, 2026"
    },
]

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    # return {"message": "Hello World!"} # fastapi automatically converts this to json
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"}) # pass data thru context dictionary (posts)

@app.get("/api/posts")
def get_posts():
    return posts