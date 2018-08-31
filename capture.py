import datetime
import sys
import os

from libs.camera import Camera
from libs.file_handler import FileHandler
from libs.email import Email

# get Duration of Video from commandline Args OR choose default if not provided
duration = 0
try:
    duration = int(sys.argv[1])
except IndexError:
    duration = 20

# Define the duration (in seconds) of the video capture here
captureDuration = duration

# Create Filename based on timestamp
# Capture time of Video
dt = datetime.datetime.today()
timestamp = dt.strftime("%Y-%m-%d_%H:%M:%S")
filePath = os.getcwd() + '/output/' + timestamp +'.avi'

# Capture and Save video on local disc
print 'Recording for {duration} seconds . . .'.format( duration=captureDuration )
cam = Camera()
cam.record(filePath, captureDuration, False)
print 'Recording completed'

# Upload File to S3
print 'Uploading file to S3 . . .'
file = FileHandler(filePath)
file.upload()
print 'File uploaded successfully, Generating Url to access video'
s3Url = file.getS3PresignedUrl();


# Email S3Url to user for viewing
print 'Sending Email . . .'
email = Email()
if(email.send('lloydsaldanha@gmail.com', file.fileBasename, s3Url)):
    print "File successfully uploaded, Email sent !"
    # file.delete()
else:
    print "something went wrong"

