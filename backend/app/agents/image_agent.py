import os

def generate_images(scenes):
    os.makedirs("backend/outputs/images", exist_ok=True)
    paths = []

    for s in scenes:
        path = f"backend/outputs/images/scene_{s['scene']}.png"
        # dummy image placeholder
        with open(path, "wb") as f:
            f.write(b"")
        paths.append(path)

    return paths
