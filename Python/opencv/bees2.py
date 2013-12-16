import cv2
rgb = cv2.imread('test1.jpg')
import numpy as np
color_image = np.asarray(rgb[:,:])

cv2.imshow('Color Image', color_image)
cv2.waitKey(0)

# Convert to Gray
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)

# Inverse Threshold Image
MAX = 255
THRESHOLD = int(gray_image.mean())
(flag, threshold_image) = cv2.threshold(gray_image, THRESHOLD, MAX, cv2.THRESH_BINARY_INV) # Binary Inverted
cv2.imshow('Threshold Image', threshold_image)
cv2.waitKey(0)

# Dilate makes white areas bigger
DILATION = 5 # need a variable method for this parameter
threshold_matrix = cv.fromarray(threshold_image)
cv.Dilate(threshold_matrix, threshold_matrix, None, DILATION)
cv2.imshow('Threshold Image', threshold_image)
cv2.waitKey(0)

# Erode makes black areas bigger
EROSION = 30 # need a variable method for this parameter
cv.Erode(threshold_matrix, threshold_matrix, None, EROSION)
cv2.imshow('Threshold Image', threshold_image)
cv2.waitKey(0)
