import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

'''
Uses the wave library to record a sine wave to a .wav file and show the wave
'''

f = 1000 # Frequency in Hertz
samples = 48000 # Number of samples to collect (.5s)
sr = 48000.0 # Sample rate in Hertz
A = 8000 # Amplitude (half the max magnitude of .wav files)
file_name = 'wavy.wav' # Name of the file to save this as

# Create a 1000 Hz sinusoid with amplitude A
sinusoid = [A*np.sin(2*np.pi*f*x/sr) for x in range(samples)]

# Configure wave library
num_frames = samples # The number of samples we're going to write
compression_type = "NONE" # We don't want to compress the data at all
compression ="not compressed" # Don't compress the data
num_channels = 1 # Only write one channel
sample_width = 2 # Writing as 16b audio, thus our width is 2 Bytes
file = wave.open(file_name, 'w') # Open the desired file
file.setparams((num_channels, sample_width, int(sr), num_frames, compression_type, compression))

# Write each sample to the .wav file
for sample in sinusoid:
    file.writeframes(struct.pack('h',int(sample))) # Pack the data into 16b

# Show a plot of the wave over two periods
period = 1 / f
x = np.linspace(0,2*period,int(sr*period*2)) # Array of 1000 linear spaced elements between [0,20]
y = np.array(sinusoid[:int(sr*period*2)])
plt.plot(x,y)
plt.show()
