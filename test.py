from libs.file_handler import FileHandler
from libs.email import Email

file = FileHandler("output/2018-08-30_16:02:49.avi")
file.upload()
s3Url = file.getS3PresignedUrl();

email = Email()
if(email.send('lloydsaldanha@gmail.com', file.fileBasename, s3Url)):
    file.delete();
    print "File successfully uploaded, Email sent !"
else:
    print "something went wrong"

