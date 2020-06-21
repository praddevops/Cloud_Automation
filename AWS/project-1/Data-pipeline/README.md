
## Objective: To read a csv file uploaded to s3 and put the contents in DynamoDB table

1) create s3 bucket
2) create dynamodb table
3) create Lambda Function
4) add permission for S3 to invoke lambda function and Create an S3 bucket event to trigger the lambda when csv file is uploaded


### Note: Role attached to Lambda function should have Read access to S3 to objects and Write access to DynamoDb
