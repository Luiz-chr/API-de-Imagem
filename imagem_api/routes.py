from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import os
from .config import UPLOAD_DIR, STATIC_DIR

router = APIRouter()

@router.get("/")
def serve_index():
    path = os.path.join(STATIC_DIR, "index.html")
    if not os.path.exists(path):
        return {"erro": "index.html não encontrado!"}
    return FileResponse(path, media_type="text/html")

@router.get("/favicon.ico", include_in_schema=False)
def favicon():
    from .static import get_favicon
    return get_favicon()

@router.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": f"Imagem '{file.filename}' salva com sucesso!"}

@router.get("/list/")
def list_images():
    return {"imagens": os.listdir(UPLOAD_DIR)}

@router.get("/search/{query}")
def search_images(query: str):
    files = os.listdir(UPLOAD_DIR)
    filtered = [f for f in files if query.lower() in f.lower()]
    return {"imagens": filtered}

@router.delete("/delete/{filename}")
def delete_image(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    os.remove(file_path)
    return {"message": f"Imagem '{filename}' deletada com sucesso!"}

@router.get("/download/{filename}")
def download_image(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    return FileResponse(file_path)
