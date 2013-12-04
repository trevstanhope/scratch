import cv2
cam = cv2.VideoCapture(1)

while True:
  (s,f) = cam.read()
  if s:
    cv2.imshow('Capture', f)
    cv2.waitKey(0)
