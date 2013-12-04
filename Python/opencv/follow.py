"""
Follow 
Trevor Stanhope
"""

import cv2, numpy, time

class Follow:

  def __init__(self, CAMERA_INDEX=0):
    try:
      self.camera = cv2.VideoCapture(CAMERA_INDEX)
    except:
      pass 
      
  def direction(self, TOLERANCE=10):
    image1 = self.capture()
    time.sleep(1)
    image2 = self.capture()
    (old, modified1) = self.get_keypoints(image1, COLOR=0) 
    (new, modified2) = self.get_keypoints(image2, COLOR=255)
    direction = []
    for a in new:
      for b in old:
        if (abs(b[0] - a[0]) < TOLERANCE) and (abs(b[1] - a[1]) < TOLERANCE):
          cv2.line(modified1, (b[0], b[1]), (a[0], a[1]), (255,255,255))
          dY = float(b[1] - a[1])
          dX = float(b[0] - a[0])
          direction.append([dX, dY])
          break
    cv2.imshow('Lines Features', modified1)
    cv2.waitKey(0)   
    return dX, dY
    
  def capture(self, CUTOFF=127):
    (success, color) = self.camera.read() # capture image as array
    if success:
      gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
      return gray
    else:
      return None
      
  def get_keypoints(self, image, THRESHOLD=1000, RADIUS=2, COLOR=255):
    surf = cv2.SURF(THRESHOLD)
    interesting, descriptors = surf.detect(image, None, useProvidedKeypoints=False)
    keypoints = []
    index = 0
    for point in interesting:
      index += 1
      x = int(point.pt[0])
      y = int(point.pt[1])
      keypoints.append([x,y])
      cv2.circle(image, (x,y), RADIUS, COLOR, -1) # draw solid circles
    cv2.imshow('Key Features', image)
    cv2.waitKey(0)
    return (numpy.array(keypoints), image)
    
if __name__ == '__main__':
  bees = Follow()
  dX,dY = bees.direction()
  print numpy.mean(dX)
  print numpy.mean(dY)
