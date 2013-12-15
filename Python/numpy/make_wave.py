import math
import wave
import struct

if __name__=='__main__':
    # http://stackoverflow.com/questions/3637350/how-to-write-stereo-wav-files-in-python
    # http://www.sonicspot.com/guide/wavefiles.html
    freq=440.0
    data_size=40000
    fname="test.wav"
    frate=11025.0 
    amp=64000.0   
    nchannels=1
    sampwidth=2
    framerate=int(frate)
    nframes=data_size
    comptype="NONE"
    compname="not compressed"
    data=[math.sin(2*math.pi*freq*(x/frate))
          for x in range(data_size)]
    wav_file=wave.open(fname, 'w')    
    wav_file.setparams((nchannels,sampwidth,framerate,nframes,comptype,compname))
    for v in data:
        wav_file.writeframes(struct.pack('h', int(v*amp/2)))
    wav_file.close()
