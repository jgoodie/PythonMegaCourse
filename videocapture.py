#!/usr/local/opt/python3/bin/python3

import cv2, time
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)
time.sleep(3)
while True:
    check, frame = video.read()
    # grey image is better for face detection
    # scale factor is usually 1.05 in most cases. Sometimes hire to avoid false positives.
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.19, minNeighbors=5)
    # add a rectangle to the face on the color image and show the image.
    for x, y, w, h in faces:
        img = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3) 
    cv2.imshow("Capture", img)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()