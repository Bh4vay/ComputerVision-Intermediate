import cv2
import easyocr

# If you want to detect text in an image 
# img = cv2.imread("test1.png")


# text detector
reader = easyocr.Reader(['en'], gpu=False)

# Realtime video capturing
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    # detect text
    text = reader.readtext(img_rgb)
    
    for t in text:
        # make rectangle
        (p1, p2, p3, p4) = t[0]
        cv2.rectangle(img, p1, p3, (0, 255, 0), 2)
        cv2.putText(img, t[1], p1, cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 0, 0), 2)
        
    cv2.imshow("Text Detection", img)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release() 
cv2.destroyAllWindows()

