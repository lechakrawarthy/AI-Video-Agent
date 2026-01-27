def generate_images(scenes):
    paths = []
    for s in scenes:
        path = f"static/images/scene_{s['scene_id']}.jpg"
        paths.append(path)
    return paths
