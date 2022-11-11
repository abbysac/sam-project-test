import boto3
import json

ec2client = boto3.client('ec2')

def lambda_handler(event, context):
    regionsRes = ec2client.describe_regions()
    return {
        "statusCode": 200,
        "body":json.dumps(
            {"message": regionsRes['Regions']}
            )
            }