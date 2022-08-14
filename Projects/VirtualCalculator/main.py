import cv2
# webcom
from cvzone.HandTrackingModule import HandDetector
import time

class Button:

    def __init__(self,pos,width, height,value):

        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self,img):

        cv2.rectangle(img, self.pos, (self.pos[0] +self.width, self.pos[1] + self.height),
                      (225, 225, 225), cv2.FILLED)

        cv2.rectangle(img, self.pos, (self.pos[0] +self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)


        cv2.putText(img, self.value, (self.pos[0] + 40 ,  self.pos[1]  + 60), cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

    def checkClick(self , x,y):

        # x1 < x < x1  + width
        if self.pos[0] < x <  self.pos[0] + self.width and \
             self.pos[1] < y <  self.pos[1] + self.height:

            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          (255, 255, 255), cv2.FILLED)

            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          (50, 50, 50), 3)

            cv2.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 80), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0),
                        2)

            return True

        else:
            return False



cap = cv2.VideoCapture(0)
cap.set(3,1280) # width
cap.set(4,720) #height

detector = HandDetector(detectionCon=0.8,maxHands=2)


#creating buttons

buttonListValues = [['7', '8','9','*'],['4', '5','6','-'],['1', '2','3','+'],['0', '/','-','=']]


buttonList  = []

for x in range(4):

    for y in range(4):

        xpos = x*100 + 800
        ypos = y* 100 + 150
        buttonList.append(Button((xpos, ypos) , 100,100,buttonListValues[y][x]))



#variables

myEq = ''
dcounter  = 0
#loop
while True:
    success,img = cap.read()
    img = cv2.flip(img ,1)

    # detection of hand
    # cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hands, img = detector.findHands(img,flipType=False)


    # draw all buttons

    cv2.rectangle(img, (800,50), (800+ 400 , 70+ 100),
                  (225, 225, 225), cv2.FILLED)

    cv2.rectangle(img, (800,50), (800+ 400 , 70+ 100),
                  (50, 50, 50), 3)

    for button in buttonList:
        button.draw(img)


    # check for hands

    if hands:
        lmList =hands[0]['lmList']
        length, _, img = detector.findDistance(lmList[8],lmList[12],img,)
        # print(length)
        x,y = lmList[8]
        if length < 50:
            for i, button in enumerate(buttonList):
                if button.checkClick(x,y) and dcounter==0:
                    myValue = buttonListValues[int(i%4)][int(i/4)]
                    if myValue == "=":
                        myEq = str(eval(myEq))
                    else:
                        myEq += myValue
                    dcounter=1


  # avoid duplicate

    if dcounter != 0:
        dcounter+=1
        if dcounter>10:
            dcounter=0





    # display equation/result
    cv2.putText(img, myEq, (810, 120), cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)


    # Display Image

    cv2.imshow("Image" , img)

    key = cv2.waitKey(1)

    if key == ord('c'):
        myEq = ""


