import boto3
import os
#import requests

class FileHandler:
    "This is a wrapper class for basic S3 interractions"

    FILE_EXPIRY = 60 * 60 * 48 # 48 hours in seconds

    filePath = None
    s3Bucket = 'rpi-remote-cctv'
    fileBasename = None
    fileName = None
    s3Key = None

    s3Url = None


    def __init__(self, filePath):
        self.filePath = filePath
        self.fileBasename = os.path.basename(filePath)
        self.fileName, extension =  os.path.splitext(self.fileBasename)
        self.s3Key = self.s3KeyGen()

    def read(self):
        "Reads a file to memory"
        fileData = None
        try:
            with open(self.filePath) as file:
                fileData = file.read()
        except:
            print('Could not open file (' + self.filePath + ')')
        return fileData


    def s3KeyGen(self):
        "Generates an S3 key"
        return self.fileBasename


    def upload(self):
        "Uploads given file to S3 bucket"
        client = boto3.client('s3')
        response = client.put_object(
            Body = self.read(),
            Bucket = self.s3Bucket,
            Key = self.s3Key
        )

        return response


    def getS3PresignedUrl(self):
        "Generates a presigned url for provided bucket and key, Url is valid for 48 hours"

        s3 = boto3.client('s3')
        self.s3Url = s3.generate_presigned_url(
            ClientMethod = 'get_object',
            Params = {
                'Bucket': self.s3Bucket,
                'Key': self.s3Key
            },
            ExpiresIn = self.FILE_EXPIRY
        )

        return self.s3Url


    def delete(self):

        if os.path.exists(self.filePath):
            os.remove(self.filePath)
        else:
            raise Exception('ERROR : File Not Found : ' + self.filePath)

