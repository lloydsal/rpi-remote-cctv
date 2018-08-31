import boto3
from botocore.exceptions import ClientError

class Email:
    sender = "Lloyd Andre Sal <lloydandresal@gmail.com>"
    awsRegion = "us-east-1"

    subject = "Your CCTV Video is ready : {fileName}"

    # The HTML body of the email.
    bodyHtml = """<html>
    <head></head>
    <body>
      <h1>Your Home CCTV Video is ready : {fileName}</h1>
      <p>Please click the below link to access your home cctv video
        <a href='{url}'>View Video</a> 
        <br/>OR copy paste the below url in your browser 
        <br/>
        <a href='{url}'>{url}</a>.</p>
    </body>
    </html>
                """
    bodyText = """Your cctv video is ready. Please open the below link to open the video.\r\n
                  File Name : {fileName}\r\n
                  Url : {url} 
                  """

    # The character encoding for the email.
    CHARSET = "UTF-8"

    def send(self, to, fileName, url):

        isSuccess = False
        # Create a new SES resource and specify a region.
        client = boto3.client('ses', region_name = self.awsRegion)

        try:
            response = client.send_email(
                Destination={
                    'ToAddresses': [to],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': self.CHARSET,
                            'Data': self.bodyHtml.format(
                                fileName = fileName,
                                url = url
                            ),
                        },
                        'Text': {
                            'Charset': self.CHARSET,
                            'Data': self.bodyText.format(
                                fileName = fileName,
                                url = url
                            ),
                        },
                    },
                    'Subject': {
                        'Charset': self.CHARSET,
                        'Data': self.subject.format(
                            fileName = fileName
                        ),
                    },
                },
                Source = self.sender,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            # print("Email sent! Message ID:"),
            # print(response['MessageId'])
            isSuccess = True

        return isSuccess

