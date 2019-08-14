#!/bin/python
import boto3
from pprint import pprint
iam_user=raw_input("Enter you IAM User name to get datials like ID,ARN,CREATION DATE: ")
session=boto3.session.Session(profile_name="dev_root")
iam_re=session.resource(service_name="iam",region_name="us-east-1")

req_iam_user=iam_re.User(iam_user)
pprint(dir(req_iam_user))
try:
#   print "IAM User: EC2_S3_IAM Detatils\nUser Name: {}\nUser Id: {}\nUser ARN: {}\nUser Creation Date: {}".format(req_iam_user.user_name,req_iam_user.user_id,req_iam_user.arn,req_iam_user.create_date)
  for eacg in req_iam_user.groups.all():
      print dir(eacg)
except Exception as e:
  print e.response['Error']['Code']
