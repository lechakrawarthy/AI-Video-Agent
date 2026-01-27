from app.agents.script_agent import generate_script
from app.agents.image_agent import generate_images
from app.agents.voice_agent import generate_voice
from app.agents.video_agent import assemble_video

def generate_video(req):
    scenes = generate_script(
        req.topic,
        req.description,
        req.duration,
        req.tone,
        req.language
    )

    images = generate_images(scenes)
    audios = generate_voice(scenes, req.voice_type)
    final_video = assemble_video(scenes, images, audios)

    return final_video
