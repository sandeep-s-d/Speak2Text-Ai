import wave
import numpy as np

def read_audio(file_path):
    wav = wave.open(file_path, 'rb')

    sample_rate = wav.getframerate()
    channels = wav.getnchannels()
    frames = wav.getnframes()

    audio_data = wav.readframes(frames)
    wav.close()

    audio_array = np.frombuffer(audio_data, dtype=np.int16)

    return sample_rate, channels, audio_array
