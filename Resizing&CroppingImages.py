import cv2
import numpy as np

img = cv2.imread("Resources/photo.jpg")
print(img.shape)

imgResize = cv2.resize(img, (300, 300))  # width  , height

imgCropped = imgResize[0:300 , 100 : 300] # array pixels managing

cv2.imshow("Image", imgCropped)

cv2.waitKey(0)
