from src.video_downloader import download_video
from src.audio_extractor import extract_audio
from src.audio_visualizer import plot_waveform
from src.audio_reader import read_audio
from src.transcriber import transcribe_audio

video_path = download_video("https://youtu.be/uSNUmJffK4c?si=LMJ6ToL4Wig2gu4m")
print("Downloaded:", video_path)

audio_path = extract_audio(video_path)
print("Extracted audio:", audio_path)



sr, ch, audio = read_audio("output.wav")
print("Sample Rate:", sr)
print("Channels:", ch)
print("Audio Samples:", len(audio))


plot_waveform(audio, sr)


print("\n--- TRANSCRIPTION ---\n")
text = transcribe_audio("output.wav")
print(text)
