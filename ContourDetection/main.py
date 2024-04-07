import cv2

img = cv2.imread("birds.jpg")
img_resized = cv2.resize(img, (1100, 680)) 
imgGray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        x1, y1, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img_resized, (x1, y1), (x1+w, y1+h), (0, 255, 0), 1)

cv2.imshow("original", img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

