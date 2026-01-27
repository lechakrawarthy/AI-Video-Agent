from pydantic import BaseModel

class VideoRequest(BaseModel):
    topic: str
    description: str
    duration: int
    tone: str
    voice_type: str
    language: str
