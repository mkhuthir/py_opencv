#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import numpy as np
import cv2 as cv

# Start Capture
cap = cv.VideoCapture(0)

# load haae cascade file
path = "xml/haarcascade_eye.xml"
eyeCascade = cv.CascadeClassifier(path)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect Eyes
    eyes = eyeCascade.detectMultiScale(gray, scaleFactor=1.01,minNeighbors=10,minSize=(10,10))
        
    # Draw circles around detected eyes
    for (x, y, w, h) in eyes:
        xc = (x + x+w)/2
        yc = (y + y+h)/2
        radius = w/2
        cv.circle(frame, (int(xc),int(yc)), int(radius), (255,0,0), 2)


    # Display the resulting frame
    cv.imshow('frame', frame)
    
    # Exit if ESC key is pressed
    if cv.waitKey(20) & 0xFF == 27:
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()