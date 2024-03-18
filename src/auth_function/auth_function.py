"""
This function is used to authorize the incoming request
"""
def lambda_handler(event, context):
    effect = 'Deny'
    if event['authorizationToken'] == 'allowme':
        effect = 'Allow'
    return {
      "principalId": 'user',
      "policyDocument":{
         "Version": "2012-10-17",
         "Statement": [
         {
          "Action": "execute-api:Invoke",
          "Resource": [event['methodArn']],
          "Effect": effect
         }
         ]
     }
    }

