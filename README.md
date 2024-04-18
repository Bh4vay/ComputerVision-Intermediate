# Object and Number Plate Detection

This project contains Detections using EasyOCR, OpenCV etc.

## Table of Contents

- [Introduction](#introduction)
- [Folder Structure](#folder-structure)

## Introduction

The project comprises two separate functionalities:

1. **Object Detection:** Utilizes YOLO (You Only Look Once) model to detect and track objects in real-time using webcam input.

2. **Number Plate Detection:** Implements license plate detection and recognition using EasyOCR and OpenCV on static images.
   
3. **Contour Detection:** Implements edge detection.

4. **Body Detection:** Implements face and eye recognition using haarcascade files as well as mediapipe.
   
5. **Color Detection:** Implements color detection in real time.

## Folder Structure

The project directory is structured as follows:


- **Object_Detection:** Contains files related to object detection functionality.
  - `yolov8n.pt`: YOLO model file for object detection.
  - `main.py`: Python script for performing object detection using the YOLO model.

- **Number_Plate_Detection:** Contains files related to number plate detection functionality.
  - `haarcascade_license_plate_rus_16stages.xml`: Cascade classifier for license plate detection.
  - `easyocr`: Directory containing EasyOCR model files (downloaded automatically).
  - `p1.jpg`: Sample image for number plate detection.
  - `main.py`: Python script for detecting and recognizing number plates in images.

- **Contour_Detection:** Contains files related to edge detection functionality.
  - `birds.jpg`: image for contour detection.
  - `main.py`: Python script for performing edge detection.

- **Body_Detection:** Contains files related to body(face and eyes) detection functionality.
  - `haarcascade_frontalface_default`: haarcascade file for face detection.
  - `haarcascade_eye`: haarcascade file for eye detection.
  - `main.py`: Python script for performing body detection.

- **Color_Detection:** Contains files related to color detection functionality.
  - `lambo.png`: image for detecting the color.
  - `main.py`: Python script for performing color detection.


