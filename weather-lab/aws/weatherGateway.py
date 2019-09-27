
import boto3
import json

print('Loading function')

my_stream_name = 'weather-data-stream'

firehose_client = boto3.client('firehose', region_name='us-east-1')

def respond(status_code, message):
    return {
        'statusCode': str(status_code),
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    put_response = firehose_client.put_record(
        DeliveryStreamName=my_stream_name,
        Record={
            'Data': json.dumps(event)
        })
    
    return ({
        "stationId" : event["stationId"],
        "status" : "OK"
    })
