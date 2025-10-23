from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="API Simples de Imagens")

# CONFIGURAÇÕES DE DIRETÓRIO

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "images")
STATIC_DIR = os.path.join(BASE_DIR, "static")
FAVICON_PATH = os.path.join(STATIC_DIR, "favicon.ico")

# Garante que as pastas existam
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)


# MIDDLEWARE DE CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# SERVE ARQUIVOS ESTÁTICOS

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


# ROTAS PRINCIPAIS


@app.get("/")
def serve_index():
    """Serve o arquivo HTML principal"""
    caminho = os.path.join(STATIC_DIR, "index.html")
    if not os.path.exists(caminho):
        return {"erro": "index.html não encontrado!", "path": caminho}
    return FileResponse(caminho, media_type="text/html")

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    """Serve o favicon para evitar 404 no navegador"""
    if os.path.exists(FAVICON_PATH):
        return FileResponse(FAVICON_PATH)
    # Caso não exista o favicon, gera um ícone temporário
    from io import BytesIO
    from PIL import Image

    img = Image.new("RGBA", (16, 16), (0, 123, 255, 255))  # azul simples
    buffer = BytesIO()
    img.save(buffer, format="ICO")
    buffer.seek(0)
    return FileResponse(buffer, media_type="image/x-icon")

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    """Upload de imagem"""
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": f"Imagem '{file.filename}' salva com sucesso!"}

@app.get("/list/")
def list_images():
    """Lista todas as imagens no diretório"""
    files = os.listdir(UPLOAD_DIR)
    return {"imagens": files}

@app.get("/search/{query}")
def search_images(query: str):
    """Busca imagens por nome parcial"""
    files = os.listdir(UPLOAD_DIR)
    filtered = [f for f in files if query.lower() in f.lower()]
    return {"imagens": filtered}

@app.delete("/delete/{filename}")
def delete_image(filename: str):
    """Deleta uma imagem específica"""
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    os.remove(file_path)
    return {"message": f"Imagem '{filename}' deletada com sucesso!"}

@app.get("/download/{filename}")
def download_image(filename: str):
    """Permite baixar uma imagem"""
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    return FileResponse(file_path)


# EXECUÇÃO DIRETA

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)