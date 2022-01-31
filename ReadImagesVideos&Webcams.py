import cv2

# Reading Image
img = cv2.imread('Resources/photo.jpg')

cv2.imshow("Output", img)
cv2.waitKey(0)  # 0 > infinite delay other means millisecond

# reading webcam , location in webcam will read video
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
