from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.models import VideoRequest
from app.orchestrator import generate_video
import os

app = FastAPI(title="AI Video Generator")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create output directories
os.makedirs("backend/outputs/videos", exist_ok=True)
os.makedirs("backend/outputs/images", exist_ok=True)
os.makedirs("backend/outputs/audio", exist_ok=True)

# Serve static files
app.mount("/backend/outputs",
          StaticFiles(directory="backend/outputs"), name="outputs")


@app.get("/")
def root():
    return {"message": "AI Video Generator API", "status": "running"}


@app.post("/generate")
def generate(req: VideoRequest):
    result = generate_video(req)
    return result
