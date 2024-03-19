import boto3
import json
import os
dynamodb_client = boto3.client('dynamodb')

"""
This function is used to insert the weather details into dynamodb
"""
def lambda_handler(event, context):
    response = ''
    status_code = 400
    req_body = event['body']
    if req_body:
        try:
            dict_body = json.loads(req_body)
            validation = validate_prerequisite(dict_body)
            if validation[0]:
                res = dynamodb_client.put_item(TableName=os.environ['TableName'], 
                                 Item={'id': {'S': dict_body['id']}, 'Weather': {'S': dict_body['weather']}})
                response = 'Successfully inserted data!'
                status_code = 200
            else:
                response = validation[1]
        except Exception as err:
            response = 'Input is not in valid format'
    else:
        response = 'Request body is absent'
    return {
         'statusCode': status_code,
         'body': response
    }

"""
This function is used to check the basic validation for the incoming request
"""  
def validate_prerequisite(dict_body):
    length = len(dict_body.keys())
    if length == 2:
       if not 'id' in dict_body or not isinstance(dict_body.get('id'), str):
           return 0, 'id is missing or id is not in the format'
       if not 'weather' in dict_body or not isinstance(dict_body.get('weather'), str):
           return 0, 'weather is missing or weather is not in the format'       
    else:
        return 0, 'Additional parameters were passed'
    return 1, ''
