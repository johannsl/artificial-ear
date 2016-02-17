import os
import soundfile
import matplotlib.pyplot

path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 
                    "resources/01.wav")
print(path)

signal, samplerate = soundfile.read(path)
print(signal)
print(samplerate)
print(matplotlib.__version__)
matplotlib.pyplot.plot(signal)
