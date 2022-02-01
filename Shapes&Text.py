import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img)

# img[:] = 255, 0, 0   # coloring images

cv2.line(img, (0, 0), (img.shape[0], img.shape[1]), (0, 255, 255), 3)
cv2.rectangle(img, (0, 0), (250, 250), (0, 0, 255), cv2.FILLED)  # rectangle : can provide color or thickness
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)  # circle

cv2.putText(img, "OpenCV", (300, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 150, 0), 3)
cv2.imshow("Image", img)

cv2.waitKey(0)
