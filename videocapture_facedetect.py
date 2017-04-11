#!/usr/local/opt/python3/bin/python3

import cv2, time
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)

check, frame = video.read()
gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.05, minNeighbors=5)
faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
for x, y, w, h in faces:
    img = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3) 
# print(check)
# print(frame)
# time.sleep(3)
resized = cv2.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))
cv2.namedWindow("Capture")
cv2.startWindowThread()
cv2.imshow("Capture", resized)
cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()


