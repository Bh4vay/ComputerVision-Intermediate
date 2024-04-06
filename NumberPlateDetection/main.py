import cv2
import easyocr
import matplotlib.pyplot as plt

img = cv2.imread("p1.jpg")
reader = easyocr.Reader(['en'], gpu=False)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plateCascade = cv2.CascadeClassifier("haarcascade_license_plate_rus_16stages.xml")

plates = plateCascade.detectMultiScale(imgGray, 1.1, 4)
for p in plates:
    x, y, w, h = p
    plate_img = img[y:y+h, x:x+w]
    text = reader.readtext(plate_img)
    for t in text:
        p1, p2, p3, p4 = t[0]
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, t[1], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    break  

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

