import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#%%
fig, ax = plt.subplots(2, 2, figsize=(12, 6))

#%%
time = np.linspace(0, 20, 20*96, endpoint=True)
freq1 = 1
amp1 = 1
comp1 = amp1 * np.cos(time*2*np.pi*freq1)
freq2 = 0.43
amp2 = 2
comp2 = amp2 * np.cos(time*2*np.pi*freq2)
comp_sum = comp1 + comp2

ax1 = ax[0, 0].twinx()
ax1.plot([0, 0.001, 19.999, 20], [0, 1, 1, 0], 'k-')
ax1.set_ylim(-1.1, 1.1)
ax[0, 0].plot(time, comp_sum)
ax[0, 0].set_ylim(-3.3, 3.3)
ax[0, 0].set_xlabel('Time [days]')
ax[0, 0].set_ylabel('Signal')

#%%
N = len(comp_sum)
T = 96
data_fft = np.fft.fft(comp_sum)[0:int(N/2)]
freq = np.fft.fftfreq(N, d=1/T)[0:int(N/2)]
amplitude = (2/N)*np.abs(data_fft)

ax[1, 0].plot(freq, amplitude, '.')
ax[1, 0].set_ylim(0, 2.1)
ax[1, 0].set_xlim(0, 1.5)
ax[1, 0].set_xlabel('Frequency [cpd]')
ax[1, 0].set_ylabel('Amplitude')

#%%
time = np.linspace(0, 20, 20*96, endpoint=True)
freq1 = 1
amp1 = 1
comp1 = amp1 * np.cos(time*2*np.pi*freq1)
freq2 = 0.43
amp2 = 2
comp2 = amp2 * np.cos(time*2*np.pi*freq2)
comp_sum = comp1 + comp2

hanning = np.hanning(len(comp_sum))

ax1 = ax[0, 1].twinx()
ax1.plot(time, hanning,'k-')
ax1.set_ylim(-1.1, 1.1)
ax1.set_ylabel('Window')
ax[0, 1].plot(time, hanning*comp_sum)
ax[0, 1].set_ylim(-3.3, 3.3)
ax[0, 1].set_xlabel('Time [days]')

#%%
N = len(comp_sum)
T = 96
data_fft = np.fft.fft(comp_sum*hanning)[0:int(N/2)]
freq = np.fft.fftfreq(N, d=1/T)[0:int(N/2)]
amplitude = 2*(2/N)*np.abs(data_fft)

ax[1, 1].plot(freq, amplitude, '.')
ax[1, 1].set_ylim(0, 2.1)
ax[1, 1].set_xlim(0, 1.5)
ax[1, 1].set_xlabel('Frequency [cpd]')
ax[1, 1].set_ylabel('Amplitude')


plt.savefig("windowing.png", dpi=300, bbox_inches='tight')