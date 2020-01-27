import cv2
import numpy as np


# The function creates a gray-scale of the image and applies GaussianBlur to reduce noise.
def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)

    return canny


def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([[(200, height), (1100, height), (550, 250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    return mask


image = cv2.imread('test_image.jpg')

# Creating a copy of the image
lane_image = np.copy(image)

canny = canny(lane_image)

# Showing the image on a new window
cv2.imshow('result', region_of_interest(canny))
cv2.waitKey(0)
