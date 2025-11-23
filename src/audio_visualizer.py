import matplotlib.pyplot as plt
import numpy as np

def plot_waveform(audio, sample_rate):
    duration = len(audio) / sample_rate
    time_axis = np.linspace(0, duration, len(audio))

    plt.figure(figsize=(12, 4))
    plt.plot(time_axis, audio)
    plt.title("Audio Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()
