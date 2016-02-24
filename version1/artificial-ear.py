
# Beat tracking example
from __future__ import print_function
import librosa
from datetime import datetime

a = datetime.now()

# 1. Get the file path to the included audio example
filename = librosa.util.example_audio_file()

b = datetime.now()
print("get file path", b-a)

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename)

c = datetime.now()
print("load audio as waveform", c-b)

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

d = datetime.now()
print("run beat tracker", d-c)

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

print('Saving output to beat_times.csv')
librosa.output.times_csv('beat_times.csv', beat_times)

e = datetime.now()
print("convert the frame indicies of beat events into timestamps", e-d)
