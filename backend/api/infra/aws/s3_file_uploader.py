# Refs
# 1. https://towardsdatascience.com/how-to-upload-and-download-files-from-aws-s3-using-python-2022-4c9b787b15f2
import logging
import os
import random

import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
from fastapi import UploadFile
from pydantic import BaseModel

logger = logging.getLogger(__name__)
boto3.set_stream_logger('boto3.resources', logging.INFO)


class S3File(BaseModel):

    # The Filename should contain the pass you want to save the file to.
    file: UploadFile
    # the exact file path of the file to be downloaded to the Key parameter.
    key: str


class AWSCredentials(BaseModel):

    access_key: str
    secret_access_key: str
    region_name: str = 'us-east-1'


class AwsBucketApi(BaseModel):

    S3_ACCESS_KEY_ID: str = os.environ.get('AWS_ACCESS_KEY_ID', None)
    S3_SECRET_ACCESS_KEY: str = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
    region_name: str = os.environ.get('AWS_REGION_NAME', None)
    bucket_name: str = os.environ.get("AWS_S3_BUCKET_NAME", None),

    def create_presigned_post(self, object_name: str,
                              fields=None, conditions=None, expiration=3600):
        """Generate a presigned URL S3 POST request to upload a file

        :param bucket_name: string
        :param object_name: string a name as which file to be stored
        :param fields: Dictionary of prefilled form fields
        :param conditions: List of conditions to include in the policy
        :param expiration: Time in seconds for the presigned URL to remain valid
        :return: Dictionary with the following keys:
            url: URL to post to
            fields: Dictionary of form fields and values to submit with the POST
        :return: None if error.
        """

        # Generate a presigned S3 POST URL
        access_key = self.S3_ACCESS_KEY_ID

        s3_client = boto3.client(
            "s3",
            aws_access_key_id=self.S3_ACCESS_KEY_ID,
            aws_secret_access_key=self.S3_SECRET_ACCESS_KEY,
            # region_name=self.region_name,
        )

        try:
            bucket_name = self.bucket_name[0]
            logger.info(bucket_name)
            response = s3_client.generate_presigned_post(
                Bucket=bucket_name,
                Key=object_name,
                ExpiresIn=10
            )

        except ClientError as e:
            logger.error(e)
            return None

        # The response contains the presigned URL and required fields
        return response


if __name__ == "__main__":
    import requests  # To install: pip install requests

    # Generate a presigned S3 POST URL
    object_path = 'backend/api/infra/aws/test.txt'
    s3_handler = AwsBucketApi()

    response = s3_handler.create_presigned_post(object_path)
    if response is None:
        exit(1)

    # Demonstrate how another Python program can use the presigned URL to upload a file
    with open(object_path, 'rb') as f:
        files = {'file': (object_path, f)}
        http_response = requests.post(response['url'], data=response['fields'], files=files)

    # If successful, returns HTTP status code 204
    print(f'File upload HTTP status code: {http_response.status_code}')
