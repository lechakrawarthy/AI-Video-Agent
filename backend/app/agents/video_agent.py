def assemble_video(scenes, images, audios):
    # Temporary mock output
    final = "backend/outputs/videos/final_video.mp4"

    # Create a dummy file so API doesn't crash
    with open(final, "wb") as f:
        f.write(b"")

    return final
