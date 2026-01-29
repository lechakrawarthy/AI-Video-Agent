from app.agents.script_agent import generate_script
from app.agents.image_agent import generate_images
from app.agents.voice_agent import generate_voice
from app.agents.video_agent import assemble_video


def generate_video(req):
    # Generate script with scenes
    scenes = generate_script(
        req.topic,
        req.description,
        req.duration,
        req.tone,
        req.language
    )

    # Generate images for each scene
    images = generate_images(scenes)

    # Generate voice narration
    audios = generate_voice(scenes, req.voice_type)

    # Assemble final video
    final_video = assemble_video(scenes, images, audios)

    # Return complete response
    return {
        "video_url": final_video,
        "scenes": scenes,
        "message": "Video generated successfully!"
    }
