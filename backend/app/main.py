import os
import shutil
import zipfile
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.services.ocr_service import OCRService
from app.services.pptx_service import PPTXService
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for Vercel/Render
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
api_key = os.getenv("UPSTAGE_API_KEY")
ocr_service = OCRService(api_key=api_key) if api_key else None
pptx_service = PPTXService()

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "message": "Server is awake and ready!"}

# Mounting Static Files

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
# Ensure absolute path for StaticFiles
ABS_OUTPUT_DIR = os.path.abspath(OUTPUT_DIR)
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(ABS_OUTPUT_DIR, exist_ok=True)

@app.post("/api/convert")
async def convert_pdf(file: UploadFile = File(...)):
    if not ocr_service:
        raise HTTPException(status_code=500, detail="OCR Service not configured (Missing API Key)")
    
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    output_filename = f"{os.path.splitext(file.filename)[0]}.pptx"
    output_location = os.path.join(OUTPUT_DIR, output_filename)
    
    # Save uploaded file
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        # 1. OCR Processing
        print(f"Starting OCR for {file.filename}...")
        ocr_result = ocr_service.parse_pdf(file_location)
        
        # 2. PPTX Generation
        print(f"Generating PPTX for {file.filename}...")
        pptx_service.create_pptx_from_ocr(file_location, ocr_result, output_location)
        
        # Return Static URL for PPTX
        encoded_filename = quote(output_filename)
        return {"download_url": f"/api/static/{encoded_filename}"}
        
    except Exception as e:
        print(f"Error processing file: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        pass

# Mount it under /api/static for easier proxying via Vite
# This allows access via http://localhost:8001/api/static/filename.pptx
app.mount("/api/static", StaticFiles(directory=ABS_OUTPUT_DIR), name="static_api")

@app.get("/")
def read_root():
    return {"message": "PDF to PPTX Converter API Ready"}
