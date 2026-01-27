from fastapi import FastAPI
from app.models import VideoRequest
from app.orchestrator import generate_video

app = FastAPI(title="AI Video Generator")

@app.post("/generate-video")
def generate(req: VideoRequest):
    video_path = generate_video(req)
    return {"video_url": video_path}
