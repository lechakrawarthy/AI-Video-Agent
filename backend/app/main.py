from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import VideoRequest
from app.orchestrator import generate_video

app = FastAPI(title="AI Video Generator")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate")
def generate(req: VideoRequest):
    video_path = generate_video(req)
    return {"video_url": video_path}
