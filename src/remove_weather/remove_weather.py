import boto3
import json
import os
dynamodb_client = boto3.resource('dynamodb')

"""
This function is used to remove the weather details from dynamodb
"""
def lambda_handler(event, context):
    req_body = event['body']
    dict_body = json.loads(req_body)
    if 'id' in dict_body:
        dynamodb_table = dynamodb_client.Table(os.environ['TableName'])
        dynamodb_table.delete_item(Key={'id': dict_body['id']})
        return {
          'statusCode': 204,
          'body': 'Successfully deleted the record'
        }
    else:
        return {
          'statusCode': 400,
          'body': 'id is missing'
        }


