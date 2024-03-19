import boto3
import json
import os
dynamodb_client = boto3.resource('dynamodb')

"""
This function is used to remove the weather details from dynamodb
"""
def lambda_handler(event, context):
    response = ''
    status_code = 400
    req_body = event['body']
    if req_body:
        try:
            dict_body = json.loads(req_body)
            if 'id' in dict_body and isinstance(dict_body['id'], str):
                dynamodb_table = dynamodb_client.Table(os.environ['TableName'])
                dynamodb_table.delete_item(Key={'id': dict_body['id']})
                response = 'Successfully deleted the record'
                status_code = 200
            else:
                response = 'id is missing or id is not in the format'
        except Exception as err:
            response = 'Input is not in valid format'
    else:
        response = 'Request body is absent'
    return {
        'statusCode': status_code,
        'body': response
    }
