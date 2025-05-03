import sounddevice as sd
from scipy.io.wavfile import write

from config import AUDIO_FILENAME, AUDIO_DURATION, SAMPLE_RATE


def record_audio(filename=AUDIO_FILENAME, duration=AUDIO_DURATION, fs=SAMPLE_RATE):
    print("Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    return filename
