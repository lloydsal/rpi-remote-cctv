import boto3
from botocore.exceptions import ClientError

class Email:
    sender = "Lloyd Andre Sal <lloydandresal@gmail.com>"
    awsRegion = "us-east-1"

    # The character encoding for the email.
    CHARSET = "UTF-8"

    def success(self, to, fileName, url):

        isSuccess = False
        # Create a new SES resource and specify a region.
        client = boto3.client('ses', region_name = self.awsRegion)

        subject = "Your CCTV Video is ready : {fileName}"
        bodyHtml = """<html>
                        <head></head>
                        <body>
                            <h1>Your Home CCTV Video is ready : {fileName}</h1>
                            <table>
                                <tr>
                                    <td style="background-color: #4ecdc4;border-color: #4c5764;border: 2px solid #45b7af;padding: 10px;text-align: center;">
                                        <a style="display: block;color: #ffffff;font-size: 12px;text-decoration: none;text-transform: uppercase;" href="{url}">
                                            Download Video
                                        </a>
                                    </td>
                                </tr>
                            </table>
                        </body>
                        </html>
            """
        bodyText = """Your cctv video is ready. Please open the below link to open the video.\r\n
                          File Name : {fileName}\r\n
                          Url : {url} 
                    """

        try:
            response = client.send_email(
                Destination={
                    'ToAddresses': [to],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': self.CHARSET,
                            'Data': bodyHtml.format(
                                fileName = fileName,
                                url = url
                            ),
                        },
                        'Text': {
                            'Charset': self.CHARSET,
                            'Data': bodyText.format(
                                fileName = fileName,
                                url = url
                            ),
                        },
                    },
                    'Subject': {
                        'Charset': self.CHARSET,
                        'Data': subject.format(
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

    def failure(self, to, timestamp):

        isSuccess = False

        # Create a new SES resource and specify a region.
        client = boto3.client('ses', region_name = self.awsRegion)

        subject = "Your CCTV Video Failed! at {timestamp}"
        bodyHtml = """<html>
                        <head></head>
                        <body>
                            <h1>Failed to Capture Video at {timestamp}</h1>
                            <p>Unable to capture your cctv video. The camera was busy or not connected. Please try again later.</p>
                        </body>
                        </html>
            """
        bodyText = "Unable to capture your cctv video (at {timestamp}). The camera was busy or not connected. Please try again later."

        try:
            response = client.send_email(
                Destination={
                    'ToAddresses': [to],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': self.CHARSET,
                            'Data': bodyHtml.format(timestamp = timestamp),
                        },
                        'Text': {
                            'Charset': self.CHARSET,
                            'Data': bodyText.format(timestamp = timestamp),
                        },
                    },
                    'Subject': {
                        'Charset': self.CHARSET,
                        'Data': subject.format(timestamp = timestamp),
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
