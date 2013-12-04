import cv2, numpy, time

cam = cv2.VideoCapture(1)
while True:
  try:
    (s,rgb) = cam.read()
    if s:
      print "success"
      hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
      sat_min = hsv[:,:,1].mean() + hsv[:,:,1].std() 
      val_min = hsv[:,:,2].mean() - hsv[:,:,2].std() 
      green_min = numpy.array([30, sat_min, val_min], numpy.uint8)
      green_max = numpy.array([90, 255, 255], numpy.uint8)
      egi = cv2.inRange(hsv, green_min, green_max)
      columns = egi.sum(axis=0)
      offset = columns.argmax()
      hsv[:,offset,:] = 255
      cv2.imshow("HSV", hsv)
      try:
        cv2.waitKey(0)
      except Exception:
        break
    else:
      print "failure"
      time.sleep(1)
      pass
  except Exception:
    cam.release()
