import numpy
from numpy import *
from PIL import Image
from cv2 import VideoCapture
import subprocess

class Cameras:
  def __init__(self):
    camera0 = VideoCapture(0)
    camera1 = VideoCapture(1)
    self.cameras = [camera0, camera1]

  def get_image(self, index):
    (success, frame) = self.cameras[index].read() # capture image as array
    if success: # if frame captured without errors
      blue = frame[:,:,2]
      green = frame[:,:,1]
      red = frame[:,:,0]
      jpeg = Image.fromarray(frame)
      jpeg.save("capture.jpg", "JPEG")
      p = subprocess.Popen(["display", "capture.jpg"])

if __name__ == '__main__':
  array = Cameras()
  array.get_image(0)
  array.get_image(1)
