# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Ruthvik Rao
# Date: 19/12/2021
# Description: Auto Stream swap wrt face on multiple streams


# Import OpenCV library
import cv2

# Initialize 3 Cameras
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(2)
cap3 = cv2.VideoCapture(1)

# Load Face Detection classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    # Read frames from each camera
    ret1, cam1 = cap1.read()
    ret2, cam2 = cap2.read()
    ret3, cam3 = cap3.read()
   
    # Convert frames to grayscale
    gray1 = cv2.cvtColor(cam1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(cam2, cv2.COLOR_BGR2GRAY)
    gray3 = cv2.cvtColor(cam3, cv2.COLOR_BGR2GRAY)
    
    # Check for Faces in each camera
    faceincam1 = face_cascade.detectMultiScale(gray1, 1.3, 5)
    faceincam2 = face_cascade.detectMultiScale(gray2, 1.3, 5)
    faceincam3 = face_cascade.detectMultiScale(gray3, 1.3, 5)
    
    # Set Default camera stream
    show_frame = cam1
    
    # Condition Statements that are to be generalized to "n" cameras
    if faceincam1 == () and faceincam2 == () and faceincam3 == ():  # If no cameras has any face, show default face
        show_frame = cam1
    elif faceincam1 != () and faceincam2 == () and faceincam3 == (): # if face found in cam1, show cam1
        show_frame = cam1
    elif faceincam1 == () and faceincam2 == () and faceincam3 != (): # if face found in cam3, show cam3
        show_frame = cam3
    elif faceincam1 == () and faceincam2 != () and faceincam3 == (): # if face found in cam2, show cam2
        show_frame = cam2

    # Show camera stream in the output window    
    cv2.imshow('Final', show_frame)
    
    # Press Q to end infinite while loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# Release all cameras and destroy output window        
cap1.release()
cap2.release()
cap3.release()
cv2.destroyAllWindows()
