import soundfile as sf
from scipy import signal

# Read .wav file
input_signal, fs = sf.read('singing.wav') 

# Sampling frequency of Input signal
sampl_freq = fs

# Order of the filter
order = 4

# Cutoff frequency 
cutoff_freq = 1000.0  

# Digital frequency
Wn = 2 * cutoff_freq / sampl_freq  

# Butterworth filter coefficients
b, a = signal.butter(order, Wn, 'low') 

# Filter the input signal with Butterworth filter using filtfilt for zero-phase filtering
output_signal = signal.filtfilt(b, a, input_signal)

# Write the output signal into .wav file
sf.write('Sound_With_ReducedNoise.wav', output_signal, fs)
print('%d',sampl_freq)
print("",a)
print("",b)

