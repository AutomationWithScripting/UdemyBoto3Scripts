import boto3
import csv
from pprint import pprint
sts_client = boto3.client('sts')
assumed_role_object=sts_client.assume_role(
    RoleArn="arn:aws:iam::943637252859:role/AWSFULLEC2",
    RoleSessionName="EC2ROLE"
)


print assumed_role_object
