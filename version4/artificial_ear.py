import librosa
import logging
import logging.config
from datetime import datetime
import math
import numpy
from utils import config
from utils import key
from utils import note
import os

def main():
    start_time = datetime.now()

    # Logging
    logging.config.dictConfig(config.LOG_CONFIG)
    log = logging.getLogger(__name__)
    log.info("Logger initiated")
    log.info(datetime.now() - start_time)

    # Load
    log.info("Loading song")
    path = os.path.join(os.path.dirname(__file__), os.pardir, "resources/01.wav")
                        #"resources/SineWave_440Hz.wav")
    signal, samplerate = librosa.load(path)
    log.info(datetime.now() - start_time)
    
    # Find BPM
    log.info("Finding BPM")
    onset_env = librosa.onset.onset_strength(signal, sr=samplerate, 
                                                aggregate=numpy.median)
    tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, 
                                                sr=samplerate)
    log.info("{:.2f}".format(tempo))
    log.info(datetime.now() - start_time)
     
    # Find list of notes
    log.info("Generating note list")
    note_list = note.generate_note_list(signal, samplerate)
    log.info(datetime.now() - start_time)

    # Find the music key
    log.info("Finding the music key")
    music_key = key.generate_key(note_list)
    log.info(datetime.now() - start_time)

if __name__ == "__main__":
    print("Project artificial ear")
    main()




