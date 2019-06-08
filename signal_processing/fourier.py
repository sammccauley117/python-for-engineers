import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

'''
Takes the Fourier Transform of a .wav file to show both time and frequency domains
'''

# Get .wav file data
samples = 48000 # Number of samples to collect (.5s)
sr = 48000.0 # Sample rate in Hertz
file_name = 'wavy.wav' # Name of the file to save this as
file = wave.open(file_name, 'r') # Open the .wav file
data = file.readframes(samples) # Read the desired number of frames (all of them)
file.close() # Close the .wav file
data = struct.unpack('{}h'.format(samples), data) # Unpack the 16b data
data = np.array(data) # Convert the data list to a np array

# Get the frequency spectra of the signal
fft_data = np.fft.fft(data) # Take the Fast Fourier Transform of the data (result is complex array)
frequencies = np.abs(fft_data) # Find the magnitude of each signal

# Plot the time domain and the frequency domain
plt.subplot(2,1,1) # Sublot 1: time
plt.plot(data[:300]) # Plot the sinusoid time data
plt.title("Time Domain") # Set subplot 1 title
plt.subplot(2,1,2) # Subplot 2: frequency
plt.plot(frequencies) # Plot the frequency data
plt.title("Frequency Domain") # Set subplot 2 title
plt.xlim(0,1200) # Only show 0Hz to 1200Hz
plt.show() # Display the plots
