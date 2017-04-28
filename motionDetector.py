#!/usr/local/opt/python3/bin/python3
# Look here: http://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/
# More: http://www.pyimagesearch.com/2015/06/01/home-surveillance-and-motion-detection-with-the-raspberry-pi-python-and-opencv/
import cv2, time, pandas
from datetime import datetime
from bokeh.plotting import figure, output_file, show
first_frame=None
# Can either declare an empty list then check if len >= 2 or init list with 2 Nones and skip the len check.
#status_list=[]
status_list=[None,None]
movement_times=[]
df = pandas.DataFrame(columns=["Start","End"])
video = cv2.VideoCapture(0)
ret = video.set(3,640)
ret = video.set(4,480)
# fourcc = cv2.VideoWriter_fourcc(*'H264')
## out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))
# sleep for a bit to let the Apple Cam to get ready.
time.sleep(3)
while True:
    check, frame = video.read()
    status = 0
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21,21),0)
    if first_frame is None:
        first_frame = gray_frame
        continue
    
    delta_frame = cv2.absdiff(first_frame, gray_frame)
    thresh_frame = cv2.threshold(delta_frame, 55, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    (_,cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        status=1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
    status_list.append(status) 
    status_list=status_list[-2:]
    # Can either declare an empty list then check if len >= 2 or init list with 2 Nones and skip the len check.
    # Check status list for movement
#     if len(status_list)>=2 and status_list[-1] == 1 and status_list[-2] == 0:
#         movement_times.append(datetime.now())
#         print("I see you!")
#     if len(status_list)>=2 and status_list[-1] == 0 and status_list[-2] == 1:
#         movement_times.append(datetime.now())
#         print("so sad, you are gone...")
    if  status_list[-1] == 1 and status_list[-2] == 0:
        movement_times.append(datetime.now())
        print("I see you!")
        # cv2.imwrite(str(datetime.now())+".jpg", frame)
        # out = cv2.VideoWriter(str(datetime.now())+'.mp4',fourcc, 20.0, (640,480))
        # out.write(frame)
    if status_list[-1] == 0 and status_list[-2] == 1:
        movement_times.append(datetime.now())
        print("so sad, you are gone...")
        # out.release()
    #cv2.imshow("grey frame", gray_frame)
    #cv2.imshow("delta frame", delta_frame)
    #cv2.imshow("thresh frame", thresh_frame)
    cv2.imshow("color frame", frame)
    key=cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            movement_times.append(datetime.now())
            # out.release()
        break
    
print(movement_times)
for i in range(0, len(movement_times),2):
    df = df.append({"Start":movement_times[i],"End":movement_times[i+1]},ignore_index=True)

df.to_csv("Movements.csv")
video.release()
print(df)
cv2.destroyAllWindows()