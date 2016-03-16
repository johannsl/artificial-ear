import librosa
import logging
import math
from numpy import asarray
from numpy import conj
from numpy import fft
from numpy import real

log = logging.getLogger(__name__)

"""
Will return a 12 item long weighted list of notes.
"""
def generate_note_list(signal, samplerate):
    note_list = [0] * 12
    frequency_range = []
    power_range = []

    signal_len = shift_bit_length(len(signal))
    factor = samplerate / float(signal_len)
    for signal_step in range(-signal_len/2, signal_len/2):
        frequency_range.append(abs(signal_step * factor))

    frequency = fft.fft(signal, signal_len)
    frequency = fft.fftshift(frequency)
    for value in frequency:
        power_range.append(value*conj(value)/signal_len)
    
    for frequency_step in range(len(frequency_range)):
        current_frequency = frequency_range[frequency_step]
        if current_frequency != 0:
            current_note = find_note(current_frequency)
            note_list[current_note] += power_range[frequency_step]

    for i in range(len(note_list)):
        note_list[i] = real(note_list[i])
    log.info(note_list)
    return note_list

"""
This is a fast way to calculate the 'next power of 2'.
It will return a number which is larger than the input number
(instead of the actual power).
shift_bit_length(15) = 16.
"""
def shift_bit_length(number):
    return 1<<(number-1).bit_length()

def find_note(frequency):
    c0 = 16.352
    exp = int(round(12 * math.log(frequency/c0, 2)))
    return exp % 12

