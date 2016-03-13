# Beat tracking example
from __future__ import print_function
import librosa
from datetime import datetime
import os
import numpy as np

path = os.path.join(os.path.dirname(__file__), os.pardir,
                        "resources/01.wav")
a = datetime.now()

# 1. Get the file path to the included audio example
filename =  path
#filename = librosa.util.example_audio_file()

b = datetime.now()
print("get file path", b-a)

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename)

c = datetime.now()
print("load audio as waveform", c-b)

# 3. Run the default beat tracker
onset_env = librosa.onset.onset_strength(y, sr=sr, aggregate=np.median)
tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

d = datetime.now()
print("run beat tracker", d-c)

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beats, sr=sr)

print('Saving output to beat_times.csv')
librosa.output.times_csv('beat_times.csv', beat_times)

e = datetime.now()
print("convert the frame indicies of beat events into timestamps", e-d)

print(librosa.util.example_audio_file())

print("total time", e-a)

import matplotlib.pyplot as plt

hop_length = 512
plt.figure()
plt.plot(librosa.util.normalize(onset_env), label='Onset strength')
plt.vlines(beats, 0, 1, alpha=0.5, color='r',
           linestyle='--', label='Beats')
plt.legend(frameon=True, framealpha=0.75)

# Limit the plot to a 15-second window
plt.xlim([10 * sr / hop_length, 25 * sr / hop_length])
plt.xticks(np.linspace(10, 25, 5) * sr / hop_length,
           np.linspace(10, 25, 5))
plt.xlabel('Time (s)')
plt.show()
