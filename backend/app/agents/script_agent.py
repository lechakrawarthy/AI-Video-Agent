def generate_script(topic, description, duration, tone, language):
    scenes_count = duration // 5
    scenes = []

    for i in range(scenes_count):
        scenes.append({
            "scene": i + 1,
            "text": f"{topic} - scene {i + 1}",
            "duration": 5
        })

    return scenes
