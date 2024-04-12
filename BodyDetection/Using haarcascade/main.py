import cv2


faceCascades = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascades = cv2.CascadeClassifier("haarcascade_eye.xml")
cap = cv2.VideoCapture(0)

while True:
    ret,img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascades.detectMultiScale(imgGray,1.1,4)
    # print(faces)
    for face in faces:
        x1,y1,w1,h1 = face
        cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(0,255,0),2)
        roi_gray = imgGray[y1:y1+h1, x1:x1+w1]
        roi_color = img[y1:y1+h1, x1:x1+w1]
        eyes = eyeCascades.detectMultiScale(roi_gray)
        for x2,y2,w2,h2 in eyes:
            cv2.rectangle(roi_color,(x2,y2),(x2+w2,y2+h2),(0,0,255),2)
        
    cv2.imshow("Detection",img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cap.release()