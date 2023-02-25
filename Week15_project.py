import boto3
import json
import time
import random

# create SQS client
sqs = boto3.client('sqs')

# create a new SQS queue
queue_name = 'md_uddin-queue'
response = sqs.create_queue(QueueName="md_uddin-queue")
queue_url = response['QueueUrl']

# define Lambda function to send message to SQS queue
def lambda_handler(event, context):
    
    # generate a random number or current time as the message body
    message_body = str(random.randint(1,100)) or str(time.time())
    
    # send message to SQS queue
    response = sqs.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/235211050898/md_uddin-queue",
        MessageBody=message_body
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello_From_sqs')
    }
