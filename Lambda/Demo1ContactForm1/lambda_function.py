import os
import json
import boto3

DYNAMODB = boto3.resource('dynamodb',os.environ['Region'])
TABLE = DYNAMODB.Table(os.environ['Table'])


def lambda_handler(event, context):
    # TODO implement
    print(event['queryStringParameters'])
    
    #save data in database
    
    item = event['queryStringParameters']
    TABLE.put_item(Item=item)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
