import cv2
import numpy as np
import time
import os


class Camera(object):

    def __init__(self):
        self.FPS = 30.0
        self.RESOLUTION = (640, 480)
        self.DEFAULT_DURATION = 20  # seconds

    def record(self, output_filepath, duration, is_display_frame=False):

        # Instantiate Camera class
        capture = cv2.VideoCapture(0)
        if (capture.isOpened() is False):
            print("Error opening video stream or file")

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')

        output = cv2.VideoWriter(output_filepath, fourcc,
                                 self.FPS, self.RESOLUTION)

        captured_frames = 0
        total_frames_required = duration*self.FPS

        while (capture.isOpened()):
            if captured_frames >= total_frames_required:
                break

            ret, frame = capture.read()

            if ret is True:
                output.write(frame)
                frame_duration = "{0}.{1}".format(int(captured_frames/self.FPS),
                                                  int(captured_frames % self.FPS))
                print("CAPTURED {0}/{1} seconds!".format(str(frame_duration),
                                                        str(duration)))
                captured_frames += 1

                # show a frame on the screen
                if(is_display_frame):
                    cv2.imshow('Frame', frame)

                # Press Q to exit
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        if captured_frames:
            print("CAPTURED {0} FRAMES!".format(str(captured_frames)))

        # Release everything if job is finished
        capture.release()
        output.release()
        cv2.destroyAllWindows()

