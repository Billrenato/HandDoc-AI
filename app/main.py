from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models
from app.ocr import process_image
from app.database import get_db, Base, engine
import os
import uuid


# Inicializa as tabelas no banco, se ainda não existirem
Base.metadata.create_all(bind=engine)

app = FastAPI(title="HandDoc AI")

@app.get("/", summary="Healthcheck")
def read_root():
    return {"message": "HandDoc AI backend está rodando 🚀"}

@app.post("/ocr/", summary="Realiza OCR em imagem e salva no banco")
async def run_ocr_and_save(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Valida formato
    if not file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
        raise HTTPException(status_code=400, detail="Formato de imagem inválido")

    # Lê imagem
    content = await file.read()

    # Gera nome único e salva localmente
    filename = f"{uuid.uuid4().hex}_{file.filename}"
    path = f"static/uploads/{filename}"
    os.makedirs("static/uploads", exist_ok=True)
    with open(path, "wb") as f:
        f.write(content)

    # Roda OCR (TrOCR ou EasyOCR no fallback)
    text = process_image(content)

    # Salva no banco
    ocr_entry = models.OCRResult(
        filename=filename,
        text=text
    )
    db.add(ocr_entry)
    db.commit()
    db.refresh(ocr_entry)

    # Retorna resposta
    return {
        "id": ocr_entry.id,
        "filename": ocr_entry.filename,
        "text": ocr_entry.text,
        "created_at": ocr_entry.created_at
    }