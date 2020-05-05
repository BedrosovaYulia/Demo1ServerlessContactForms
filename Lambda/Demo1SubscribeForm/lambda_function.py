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
    
    #send email
    response = SES.send_email(
        Destination={
            'ToAddresses': [
            item['email'],
            ],
            'CcAddresses': [
                'y@bedrosova.ru',
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': 'UTF-8',
                    'Data': 'This message body contains HTML formatting. It can, for example, contain links like this one: <a class="ulink" href="http://docs.aws.amazon.com/ses/latest/DeveloperGuide" target="_blank">Amazon SES Developer Guide</a>.',
                },
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': 'This is the message body in text format.',
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Test email',
            },
        },
        Source='y@bedrosova.ru'
    )
    
    print(response)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
