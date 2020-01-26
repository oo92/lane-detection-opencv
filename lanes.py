import cv2
import numpy as np

image = cv2.imread('test_image.jpg')

# Creating a copy of the image and turning that image into gray scale
lane_image = np.copy(image)
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

# Reducing noise in the image
blur = cv2.GaussianBlur(gray, (5, 5), 0)
canny = cv2.Canny(blur, 50, 150)

# Showing the image on a new window
cv2.imshow('result', canny)
cv2.waitKey(0)
