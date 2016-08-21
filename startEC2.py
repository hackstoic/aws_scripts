import boto3
import logging

#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# AWS credentials
ACCESS_KEY = "AKIAxxxxxxxxxexample"
SECRET_KEY = "qae6xxxxxxxxxexample"

#define the connection
ec2 = boto3.client(
    'ec2',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)

InstanceIds=[
        'your_instance_id',
]

def lambda_handler(event, context):
    response = ec2.start_instances(
        DryRun=False,
        InstanceIds=InstanceIds,
        Force=False
    )
    logger.info(response)
    return InstanceIds
