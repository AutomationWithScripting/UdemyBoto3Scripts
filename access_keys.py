#!/bin/python
import boto3
from botocore.exceptions import ClientError
import datetime

def get_usr_old_keys(key_age):
  session=boto3.session.Session(profile_name="dev_root")
  iam_client = session.client('iam',region_name='us-east-1')
  
  

def lambda_handler(event, context):
  key_age=90
  snstopicarn=""
  return get_usr_old_keys( key_age )


print lambda_handler(None,None)
