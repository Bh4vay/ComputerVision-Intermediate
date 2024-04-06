# Object and Number Plate Detection

This project contains two main functionalities: Object Detection using YOLO (You Only Look Once) model and Number Plate Detection using EasyOCR and OpenCV.

## Table of Contents

- [Introduction](#introduction)
- [Folder Structure](#folder-structure)

## Introduction

The project comprises two separate functionalities:

1. **Object Detection:** Utilizes YOLO (You Only Look Once) model to detect and track objects in real-time using webcam input.

2. **Number Plate Detection:** Implements license plate detection and recognition using EasyOCR and OpenCV on static images.

## Folder Structure

The project directory is structured as follows:


- **Object_Detection:** Contains files related to object detection functionality.
  - `yolov8n.pt`: YOLO model file for object detection.
  - `object_detection.py`: Python script for performing object detection using the YOLO model.

- **Number_Plate_Detection:** Contains files related to number plate detection functionality.
  - `haarcascade_license_plate_rus_16stages.xml`: Cascade classifier for license plate detection.
  - `easyocr`: Directory containing EasyOCR model files (downloaded automatically).
  - `p1.jpg`: Sample image for number plate detection.
  - `number_plate_detection.py`: Python script for detecting and recognizing number plates in images.


