import subprocess


def create_scene_video(image, audio, duration, output):
subprocess.run([
"ffmpeg", "-y",
"-loop", "1", "-i", image,
"-i", audio,
"-t", str(duration),
"-vf", "scale=1080:1920",
"-c:v", "libx264",
"-c:a", "aac",
output
])