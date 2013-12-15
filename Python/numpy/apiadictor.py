#!/usr/bin/env python
# Record ambient hum amplitude
import alsaaudio, wave, numpy, time, csv

# Constants
CHANNEL = 1
CHANNELS = 1
RATE = 44100
CHUNK = 1024
AMP_WIDTH = 2

# Microphone
microphone = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
microphone.setchannels(CHANNEL)
microphone.setrate(RATE)
microphone.setformat(alsaaudio.PCM_FORMAT_S16_LE)
microphone.setperiodsize(CHUNK)

# Listen
while True:
  print('-------------')
  (success, data) = microphone.read()
  if success:
    try:
      wave_array = numpy.fromstring(data, dtype='int16')
      wave_list = wave_array.tolist()
      wave_fft = numpy.fft.fft(wave_array)
      wave_freqs = numpy.fft.fftfreq(len(wave_fft))
      maxima = numpy.argmax(numpy.abs(wave_fft)**2)
      freq = wave_freqs[maxima]
      freq_in_hertz = abs(freq*RATE)
      amplitude = numpy.sqrt(numpy.mean(numpy.abs(wave_fft)**2))
      decibels = 20*numpy.log10(amplitude)
      print('Frequency (Hz): ' + str(freq_in_hertz))
      print('Sound (dB): ' + str(decibels))
    except ValueError as error:
      print str(error)
      pass
