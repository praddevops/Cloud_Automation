"""
Boto3 python script to add permission for s3 to invoke lambda and also send a notification to lambda function when a csv file is uploaded to s3 bucket
Required 3rd party python packages that can be installed with pip: boto3, docopt
python3 -m pip install <package-name>

Usage: 
  put_bucket_notification.py <BucketName> -l lambda_fn_name -a aws_acc_id -r aws_region
  put_bucket_notification.py -h | --help

Options:
  -l lambda_fn_name
  -a aws_acc_id
  -r aws_region
  -h --help
"""

import boto3
from docopt import docopt

bucket_name = None
lambda_arn = None

if __name__ == '__main__':
    arguments = docopt(__doc__)
    if arguments["<BucketName>"] != None:
        bucket_name = arguments["<BucketName>"]
    if arguments["-l"] != None:
        lambda_function_name = arguments["-l"]
    if arguments["-a"] != None:
        aws_account_id = arguments["-a"]
    if arguments["-r"] != None:
        region = arguments["-r"]


lambda_client = boto3.client('lambda')

try:
    permit_s3_lambda = lambda_client.add_permission(
        Action='lambda:InvokeFunction',
        FunctionName=lambda_function_name,
        Principal='s3.amazonaws.com',
        SourceAccount=aws_account_id,
        SourceArn='arn:aws:s3:::'+bucket_name,
        StatementId='s3',
    )
except Exception as e:
    print("S3 bucket already has permission to invoke lambda")

aws_s3_client = boto3.client('s3')

response = aws_s3_client.put_bucket_notification_configuration(
    Bucket=bucket_name,
    NotificationConfiguration={
        
        'LambdaFunctionConfigurations': [
            {
               #Optional 'Id': 'string',
                'LambdaFunctionArn': "arn:aws:lambda:"+region+":"+aws_account_id+":function:"+lambda_function_name, #Required
                'Events': [
                    's3:ObjectCreated:*',
                ],
                'Filter': {
                    'Key': {
                        'FilterRules': [
                            {
                                'Name': 'suffix',
                                'Value': '.csv'
                            },
                        ]
                    }
                }
            },
        ]
    }
)