from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from .config import STATIC_DIR, FAVICON_PATH
import os

def setup_static(app):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

def get_favicon():
    if os.path.exists(FAVICON_PATH):
        return FileResponse(FAVICON_PATH)

    from io import BytesIO
    from PIL import Image

    img = Image.new("RGBA", (16, 16), (0, 123, 255))
    buffer = BytesIO()
    img.save(buffer, format="ICO")
    buffer.seek(0)
    return FileResponse(buffer, media_type="image/x-icon")
