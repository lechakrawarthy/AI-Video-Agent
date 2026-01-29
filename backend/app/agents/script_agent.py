def generate_script(topic, description, duration, tone, language):
    """
    Generate a script broken into scenes based on duration.
    In production, this would use OpenAI API to generate actual content.
    """
    scenes_count = max(1, duration // 5)  # At least 1 scene
    scenes = []

    for i in range(scenes_count):
        scene_number = i + 1
        scenes.append({
            "scene": scene_number,
            "text": f"{topic}: {description} - Part {scene_number} ({tone} tone)",
            "duration": min(5, duration - (i * 5))
        })

    return scenes
