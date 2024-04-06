from ultralytics import YOLO

import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open webcam
video = cv2.VideoCapture(0)
video.set(3, 500)
video.set(4, 450)

while True:
    # Read frame from webcam
    ret, img = video.read()

    # Perform object tracking
    results = model.track(img, persist=True)

    # Plot tracked objects on the frame
    img_ = results[0].plot()

    # Display the frame
    cv2.imshow("Frames", img_)

    # Exit if 'x' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# Release video capture and close windows
video.release()
cv2.destroyAllWindows()

