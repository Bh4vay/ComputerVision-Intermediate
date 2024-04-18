import cv2
import numpy as np

# Specify the range of Hue, Saturation and Value for the colour you want (For now let's take red) Confirm form google!
lower = np.array([0,70,50])
upper = np.array([10,255,255])

cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    
    # CONVERT TO HSV - for colour detection
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(imgHSV,lower,upper)
    
    # making a rectangular box around the image
    countours ,  hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in countours:
        if cv2.contourArea(cnt)>500:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    

    cv2.imshow("Original",img)
    cv2.imshow("Mask",mask)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cap.release()