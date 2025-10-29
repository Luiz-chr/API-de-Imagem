import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "../images")
STATIC_DIR = os.path.join(BASE_DIR, "../static")
FAVICON_PATH = os.path.join(STATIC_DIR, "favicon.ico")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)
