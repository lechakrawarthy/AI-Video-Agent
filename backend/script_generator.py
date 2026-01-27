def generate_script(data):
    return (
        f"This video is about {data.topic}. "
        f"{data.description}. "
        f"The tone is {data.tone}."
    )
