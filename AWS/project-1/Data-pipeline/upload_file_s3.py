"""
Boto3 python script to upload file to an S3 bucket
Required 3rd party python packages that can be installed with pip: boto3, botocore, docopt
python3 -m pip install <package-name>

Usage: 
   upload_file_s3.py -f File -b BucketName
   upload_file_s3.py -h | --help

Options:
  -h --help
  -f File # file to upload to the bucket
  -b BucketName # Bucket to which file will be uploaded
"""

import logging
import boto3
from docopt import docopt
from botocore.exceptions import ClientError

file_name = None
bucket = None

if __name__ == '__main__':
    arguments = docopt(__doc__)
    if arguments["-f"] != None:
        file_name = arguments["-f"]
    if arguments["-b"] != None:
        bucket = arguments["-b"]


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

upload_file(file_name, bucket)
