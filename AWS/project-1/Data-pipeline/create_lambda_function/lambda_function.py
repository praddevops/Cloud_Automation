import boto3
s3_client = boto3.client('s3')

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('mytable_123')

#WIP
def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    s3_file_name = event['Records'][0]['s3']['object']['key']
    resp = s3_client.get_object(Bucket=bucket_name,Key=s3_file_name)
    data = resp['Body'].read().decode("utf-8")
    table_data = data.split("\\n")
    for item in table_data:
        item_data = item.split(",")
        
       # print("    id            name       location")
       # print (item_data[0]+"   "+item_data[1]+" "+item_data[2])
        
        #insert in dynamodb table
        try:    
            table.put_item(
                Item = {
                    "id": item_data[0],
                    "name": item_data[1],
                    "location": item_data[2]
                }
            )
        except Exception as e:
            print("End of File")