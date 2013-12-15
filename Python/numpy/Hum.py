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

# Wave
wavefile = wave.open('test.wav', 'w')
wavefile.setnchannels(CHANNELS)
wavefile.setsampwidth(AMP_WIDTH)
wavefile.setframerate(RATE)

# Listen
while True:
  print('-------------')
  (success, data) = microphone.read()
  if success:
    wavefile.writeframes(data)
    try:
      wave_array = numpy.fromstring(data, dtype='int16')
      wave_list = wave_array.tolist()
      wave_fft = numpy.fft.fft(wave_array)
      wave_freqs = numpy.fft.fftfreq(len(wave_fft))
      maxima = numpy.argmax(numpy.abs(wave_fft)**2)
      freq = wave_freqs[maxima]
      freq_in_hertz = abs(freq*RATE)
      print(freq_in_hertz)
      with open('some.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(wave_list)
    except ValueError:
      print('Bad wave')
      time.sleep(1)
  else:
    print('Bad capture')
    time.sleep(1)
    
