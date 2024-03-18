# cygnum
Mini Project using sam cli in which the flow will be like apigateway -> lambda -> Dynamodb

## Steps to follow
* Signup aws free tier account
* Create one user & get the access key and secret key for that user
* Make sure whether the user has proper permission for the aws resources which are going to use in this project
* Install aws cli locally
* Configure aws credentials locally
* Install sam cli locally

## Installation for awscli
* sudo apt install awscli

## Installation for samcli
* Download https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip
* unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
* sudo ./sam-installation/install

## Stack name for this project
SamCygnum

## Commands for stack Deployment
* sam deploy --guided

## Commands for stack Deletion
* aws cloudformation delete-stack --stack-name SamCygnum


