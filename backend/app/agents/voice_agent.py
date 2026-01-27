import os

def generate_voice(scenes, voice_type):
    os.makedirs("backend/outputs/audio", exist_ok=True)
    files = []

    for s in scenes:
        path = f"backend/outputs/audio/scene_{s['scene']}.mp3"
        # dummy audio placeholder
        with open(path, "wb") as f:
            f.write(b"")
        files.append(path)

    return files
