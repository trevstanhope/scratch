import cv2
rgb = cv2.imread('test1.jpg')
import numpy

hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
sat_min = hsv[:,:,1].mean()
val_min = hsv[:,:,2].mean()
GREEN_MIN = numpy.array([0, 0, val_min], numpy.uint8)
GREEN_MAX = numpy.array([360, 255, 255], numpy.uint8)
egi = cv2.inRange(hsv, GREEN_MIN, GREEN_MAX)
surf = cv2.SURF(10000)
(bees, descriptors) = surf.detect(egi, None, useProvidedKeypoints=False)
index = 0
for bee in bees:
	print descriptors[index]
	x = int(bee.pt[0])
	y = int(bee.pt[1])
	cv2.circle(rgb, (x,y), 5, (0,0,255), 1)
	index += 1
cv2.imshow('bees', rgb)
cv2.waitKey(0)
cv2.imshow('bees', egi)
cv2.waitKey(0)
