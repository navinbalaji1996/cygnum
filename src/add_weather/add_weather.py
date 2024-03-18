import boto3
import json
import os
dynamodb_client = boto3.client('dynamodb')

"""
This function is used to insert the weather details into dynamodb
"""
def lambda_handler(event, context):
    req_body = event['body']
    dict_body = json.loads(req_body)
    validation = validate_prerequisite(dict_body)
    if validation[0]:
        dynamodb_client.put_item(TableName=os.environ['TableName'], 
                                 Item={'id': {'S': dict_body['id']}, 'Weather': {'S': dict_body['weather']}})
        return {
          'statusCode': 200,
          'body': 'Successfully inserted data!'
        }
    else:
        return {
          'statusCode': 400,
          'body': validation[1]
        }

"""
This function is used to check the basic validation for the incoming request
"""  
def validate_prerequisite(dict_body):
    length = len(dict_body.keys())
    if length == 2:
       if not 'id' in dict_body:
           return 0, 'id is missing'
       if not 'weather' in dict_body:
           return 0, 'weather is missing'       
    else:
        return 0, 'Additional parameters were passed'
    return 1, ''
