🛠️ Description
Face Detection using OpenCV

This project implements face detection with OpenCV. It includes installation instructions, required imports, and version details.

Installation

Install Python from python.org.

Install OpenCV using pip:


pip install opencv-python

Imports

To use this project's face detection, import the following module:

import cv2

Usage

Clone or download the source code.

Create a new Python file in your IDE/editor.

Import the necessary module:


import cv2

Load the pre-trained face detection model:

face_cascade = cv2.CascadeClassifier('path/to/haarcascade_frontalface_default.xml')

capture video frames:



cap = cv2.VideoCapture(0)
Detect faces:

faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
Process detected faces as needed.

Display the video frames:

cv2.imshow('Face Detection', video)
cv2.waitKey(0)
cv2.destroyAllWindows()


Versions

Developed with:

OpenCV 4.8.0.76
Python 3.9.13
