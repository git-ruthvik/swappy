# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Ruthvik Rao
# Date: 19/12/2021
# Description: Auto Stream swap wrt face on multiple streams



import cv2
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(2)
cap3 = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    ret1, cam1 = cap1.read()
    ret2, cam2 = cap2.read()
    ret3, cam3 = cap3.read()
    gray1 = cv2.cvtColor(cam1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(cam2, cv2.COLOR_BGR2GRAY)
    gray3 = cv2.cvtColor(cam3, cv2.COLOR_BGR2GRAY)
    faceincam1 = face_cascade.detectMultiScale(gray1, 1.3, 5)
    faceincam2 = face_cascade.detectMultiScale(gray2, 1.3, 5)
    faceincam3 = face_cascade.detectMultiScale(gray3, 1.3, 5)
    show_frame = cam1
    if faceincam1 == () and faceincam2 == () and faceincam3 == ():
        show_frame = cam1
    elif faceincam1 != () and faceincam2 == () and faceincam3 == ():
        show_frame = cam1
    elif faceincam1 == () and faceincam2 == () and faceincam3 != ():
        show_frame = cam3
    elif faceincam1 == () and faceincam2 != () and faceincam3 == ():
        show_frame = cam2

    cv2.imshow('Final', show_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap1.release()
cap2.release()
cap3.release()
cv2.destroyAllWindows()
