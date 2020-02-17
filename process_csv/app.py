import json
import pandas as pd
import boto3
import os
from io import StringIO
from urllib.parse import unquote_plus

s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')
bucket = os.environ['S3Bucket']

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        df = pd.read_csv('s3://'+bucket+'/'+key)
        # do some work
        df = df.corr()
        print(df.head(1))
        
        csv_buffer = StringIO()
        df.to_csv(csv_buffer)
        s3_resource.Object(bucket, 'processed/'+key.replace('raw/','')).put(Body=csv_buffer.getvalue())
        
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
