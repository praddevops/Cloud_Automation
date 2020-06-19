"""
Boto3 python script to create s3 bucket
Required 3rd party python packages that can be installed with pip: boto3, botocore, docopt
python3 -m pip install <package-name>

Usage: 
  create_s3_bucket.py <BucketName> [-r Bucketregion]
  create_s3_bucket.py -h | --help

Options:
  -h --help
  -r BucketRegion # Bucket region (Optional) 
"""
import logging
import boto3
import json
from docopt import docopt
from botocore.exceptions import ClientError


bucket_name = None
region = None

if __name__ == '__main__':
    arguments = docopt(__doc__)
    if arguments["<BucketName>"] != None:
        bucket_name = arguments["<BucketName>"]
        print ("Bucket name set to: "+bucket_name)
    if arguments["-r"] != None:
        region = arguments["-r"]
        print ("Bucket Region set to: "+region)



def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

create_bucket(bucket_name, region)

# Create a bucket policy

bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': f'arn:aws:s3:::{bucket_name}/*'
    }]
}

# Convert the policy from JSON dict to string
bucket_policy = json.dumps(bucket_policy)

# Set the new policy
s3 = boto3.client('s3')
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)