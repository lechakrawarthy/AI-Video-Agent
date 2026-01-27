from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from script_generator import generate_script
from scene_planner import create_scenes
from image_generator import generate_images
from voice_generator import generate_voice
from video_builder import build_video
from caption_generator import generate_captions

app = FastAPI()
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    topic: str
    description: str
    duration: int
    tone: str
    voice: str
    language: str

@app.post("/generate")
def generate_video(data: VideoRequest):
    script = generate_script(data)
    scenes = create_scenes(script, data.duration)
    images = generate_images(scenes)
    audio = generate_voice(scenes)
    video_path = build_video(images, audio)
    captions = generate_captions(scenes)

    return {
        "script": script,
        "scenes": scenes,
        "video": video_path,
        "captions": captions
    }
