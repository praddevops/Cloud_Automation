

import boto3
from docopt import docopt

lambda_fn_name = "my_lambda_etl"

deploymentPackage = "deployment.zip"

aws_lambda_client = boto3.client('lambda')

with open(deploymentPackage, mode='rb') as file: 
    lambda_deployment_package = file.read()

response = aws_lambda_client.create_function(
    FunctionName=lambda_fn_name,
    Runtime='python3.7',
    Role='arn:aws:iam::745515453056:role/Lambda_S3_Full_Access_Role', # Role ARN
    Handler='lambda_function.lambda_handler',
    Code={
        'ZipFile': lambda_deployment_package,
        #'S3Bucket': 'string',
        #'S3Key': 'string',
        #'S3ObjectVersion': 'string'
    },
    Description='Lambda Function to transform csv data into DynamoDB table',
    Timeout=120,
    MemorySize=128,
    Publish=True,
)

print("Lambda Function ARN: "+response['FunctionArn'])