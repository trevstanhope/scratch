"""
Webcam to CSV
Description: Captures video from a webcam and saves the bands as csv.
Author: Trevor Stanhope
Requires: Python 2.x, NumPy, OpenCV
License: MIT
"""

import numpy
from numpy import *
import cv2
import time

class Camera:
  def __init__(self):
    self.camera = cv2.VideoCapture(0)

  def get_image(self):
    (success, frame) = self.camera.read() # capture image as array
    if success: # if frame captured without errors
      print('Captured Image!')
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      return gray
    else:
      print('Failed to Capture Image!')
      empty = numpy.zeros((480,640))
      return empy
  
  def to_csv(self, band, filename):
    print('Writing to CSV: ' + filename)
    with open(filename, 'w') as csvfile:
      (h,w) = band.shape
      for y in range(h):
        for x in range(w):
          csvfile.write(str(band[y,x]) + ',')
        csvfile.write('\n')

if __name__ == '__main__':
  camera = Camera()
  while True:
    try:
      gray = camera.get_image()
      camera.to_csv(gray,'gray.csv')
    except KeyboardInterrupt as error:
      break
