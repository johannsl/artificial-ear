import librosa
import math

tone_ratio = []

def find_note(freq):
    c0 = 16.352
    exp = int(round(12 * math.log(freq/c0, 2)))
    return exp % 12

signal, samplerate = librosa.load
