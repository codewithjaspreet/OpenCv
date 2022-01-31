import cv2
import numpy as np

img = cv2.imread('Resources/photo.jpg')
kernel = np.ones((5, 5), np.uint8)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# change color of image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# blur images
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)  # thickness
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)  # thinness
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDialation)
cv2.imshow("Erosion Image", imgEroded)
cv2.waitKey(0)
