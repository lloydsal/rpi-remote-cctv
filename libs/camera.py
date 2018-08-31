import cv2
import numpy as np
import time

class Camera:

    FPS = 30.0
    RESOLUTION = (640, 480)
    DEFAULT_DURATION = 20 # seconds
    isDisplayFrame = False

    duration = None

    def record(self, outputFilePath, duration, isDisplayFrame = False):

        self.duration = duration
        self.isDisplayFrame = isDisplayFrame

        # Instantiate Camera class
        cap = cv2.VideoCapture(0)
        # cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 100)
        # cap.set(cv2.CAP_PROP_EXPOSURE, 1000)

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # fourcc = cv2.VideoWriter_fourcc(*'MJPG')

        out = cv2.VideoWriter(outputFilePath, fourcc, self.FPS, self.RESOLUTION)

        startTime = time.time()
        while (int(time.time() - startTime) <= self.duration):
            ret, frame = cap.read()

            if ret == True:
                out.write(frame)

                # show a frame on the screen
                if(self.isDisplayFrame == True or self.isDisplayFrame == 1):
                    cv2.imshow('frame', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        # Release everything if job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()