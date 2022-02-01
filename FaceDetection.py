import numpy as np
import cv2
# face - detection usin
img = cv2.imread('Resources/photo.jpg')
facecCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
imgResize = cv2.resize(img,(300,300))
imgGray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)

faces = facecCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(imgResize, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Result", imgResize)
cv2.waitKey(0)
