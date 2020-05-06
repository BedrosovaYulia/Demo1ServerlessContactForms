import os
import json
import boto3

DYNAMODB = boto3.resource('dynamodb',os.environ['Region'])
TABLE = DYNAMODB.Table(os.environ['Table'])
SES = boto3.client('ses')


def lambda_handler(event, context):
    # TODO implement
    print(event['queryStringParameters'])
    
    #save data in database
    item=dict()
    item['email'] = event['queryStringParameters']['emailsub']
    TABLE.put_item(Item=item)
    
    response = SES.verify_email_identity(
        EmailAddress=item['email']
    )
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
