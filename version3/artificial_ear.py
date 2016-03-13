import librosa
import logging
import logging.config
import math
from numpy import conj
from numpy import fft
from utils import config
import os

def main():
    # Logging
    logging.config.dictConfig(config.LOG_CONFIG)
    log = logging.getLogger(__name__)
    log.info("Logger initiated")
    
    path = os.path.join(os.path.dirname(__file__), os.pardir, "resources/01.wav") 
    signal, samplerate = librosa.load(path)
    signal_len = next_pow_2(len(signal))
    freq0 = fft.fft(signal, signal_len)
    freq1 = fft.fftshift(freq0)
    freq_range = []
    factor = samplerate / float(signal_len)
    for signal in range(-signal_len/2, signal_len/2):
        freq_range.append(abs(signal * factor))
    power = []
    for value in freq1:
        power.append((value*conj(value))/signal_len)
    note_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(freq_range)):
        freq = freq_range[i]
        if freq != 0:
            note = find_note(freq)
            note_list[note] += power[i]
    log.info(note_list)

def find_note(freq):
    c0 = 16.352
    exp = int(round(12 * math.log(freq/c0, 2)))
    return exp % 12

def next_pow_2(number):
    return int(2**math.ceil(math.log(abs(number), 2)))



if __name__ == "__main__":
    print("Project artificial ear")
    main()
