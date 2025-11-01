from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from .config import STATIC_DIR, FAVICON_PATH
import os

def setup_static(app):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

def get_favicon():
    if os.path.exists(FAVICON_PATH):
        return FileResponse(FAVICON_PATH, media_type="image/x-icon")
    return {"error": "favicon.ico não encontrado"}
