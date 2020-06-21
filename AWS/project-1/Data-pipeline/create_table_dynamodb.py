"""
Boto3 python script to create dynamodb table
Required 3rd party python packages that can be installed with pip: boto3, botocore, docopt
python3 -m pip install <package-name>

Usage: 
  create_table_dynamodb.py -t table_name
  create_table_dynamodb.py -h | --help

Options:
  -h --help
  -t table_name # Bucket name 
"""


import boto3
from docopt import docopt

table_name = 'my_table123'

if __name__ == '__main__':
    arguments = docopt(__doc__)
    if arguments["-t"] != None:
        table_name = arguments["-t"]

def create_dynamodb_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.client('dynamodb')

    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'location',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'id',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'location',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__':
    dynamodb_table = create_dynamodb_table()