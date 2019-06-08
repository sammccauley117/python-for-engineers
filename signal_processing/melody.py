import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

'''
Uses the wave library to create a simple melody
'''

# Create a dictionary for notes -> frequency
notes = {
    'c' : 261,
    'd' : 294,
    'e' : 329,
    'f' : 349,
    'g' : 392,
    'a' : 440,
    'b' : 493,
    'C' : 523,
}
samples = 24000 # Number of samples to collect for each note (.5s)
sr = 48000.0 # Sample rate in Hertz
A = 8000 # Amplitude (volume) (1/4 the max magnitude of .wav files)
file_name = 'melody.wav' # Name of the file to save this as
melody = ['e','d','c','d','e','e','e','d','d','d','e','e','e']

# Create the melody
song = []
for note in melody:
    f = notes[note]
    song += [A*np.sin(2*np.pi*f*x/sr) for x in range(samples)]

# Configure wave library
num_frames = len(melody) * samples # The number of samples we're going to write
compression_type = "NONE" # We don't want to compress the data at all
compression ="not compressed" # Don't compress the data
num_channels = 1 # Only write one channel
sample_width = 2 # Writing as 16b audio, thus our width is 2 Bytes
file = wave.open(file_name, 'w') # Open the desired file
file.setparams((num_channels, sample_width, int(sr), num_frames, compression_type, compression))

# Write each sample to the .wav file
for sample in song:
    file.writeframes(struct.pack('h',int(sample))) # Pack the data into 16b
