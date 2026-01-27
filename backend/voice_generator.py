def generate_voice(scenes):
    paths = []
    for s in scenes:
        path = f"static/audio/scene_{s['scene_id']}.mp3"
        paths.append(path)
    return paths
