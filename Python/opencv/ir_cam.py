import cv2, numpy

cam = cv2.VideoCapture(1)
while True:
  (s,f) = cam.read()
  if s:
    b = f[:,:,0]
    g = f[:,:,1]
    r = f[:,:,2]
    gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    print
    print('Shape: ' + str(gray.shape))
    print('Max: ' + str(gray.max()))
    print('Mean: ' + str(gray.mean()))
    print('Min: ' + str(gray.min()))
    print('STD: ' + str(gray.std()))
  
