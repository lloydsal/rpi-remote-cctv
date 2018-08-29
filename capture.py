import numpy as np
import cv2
import time
import datetime
import sys

duration = 0
try:
    duration = int(sys.argv[1])
except IndexError:
    duration = 20

# Define the duration (in seconds) of the video capture here
captureDuration = duration

# Capture time of Video
dt = datetime.datetime.today()
timestamp = dt.strftime("%Y-%m-%d_%H:%M:%S")

cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 100)
# cap.set(cv2.CAP_PROP_EXPOSURE, 1000)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output/' + timestamp +'.avi', fourcc, 30.0, (640,480))

startTime = time.time()

while( int(time.time() - startTime) <= captureDuration ):
    ret, frame = cap.read()
    if ret==True:

        out.write(frame)

        # show a frame on the screen
#        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
