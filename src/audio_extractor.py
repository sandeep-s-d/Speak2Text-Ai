import subprocess
import os

def extract_audio(video_path, output_audio="output.wav"):
    # 1. Check if video exists
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"File not found: {video_path}")

    # 2. Build ffmpeg command
    command = [
    "ffmpeg",
    "-y",                      # <--- ADD THIS
    "-i", video_path,
    "-vn",
    "-acodec", "pcm_s16le",
    "-ar", "16000",
    "-ac", "1",
    output_audio
]


    # 3. Run ffmpeg
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # 4. Verify output file created
    if not os.path.exists(output_audio):
        raise Exception("Audio extraction failed")

    return output_audio
