"""
Boto3 python script to create dynamodb table
Required 3rd party python packages that can be installed with pip: boto3, botocore, docopt
python3 -m pip install <package-name>

Usage: 
  create_table_dynamodb.py -b Buckt_name
  create_table_dynamodb.py -h | --help

Options:
  -h --help
  -b Buckt_name # Bucket name 
"""


import boto3
from docopt import docopt

table_name = 'my_table'

if __name__ == '__main__':
    arguments = docopt(__doc__)
    if arguments["-b"] != None:
        table_name = arguments["-b"]

def create_dynamodb_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.client('dynamodb')

    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
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