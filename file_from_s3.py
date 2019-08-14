#!/usr/bin/python
try:
  import boto3
  print "Successfully imported boto3"
except:
  print "unable to import boto3"

#session=boto3.session.Session(profile_name="EC2_S3_IAM")
#s3_con_re=session.resource(service_name="s3",region_name="us-east-1")
#s3_con_cli=session.client(service_name="s3",region_name="us-east-1")

s3_con_cli=boto3.session.Session(profile_name="EC2_S3_IAM").client(service_name="s3",region_name="us-east-1")


for each_bucket in s3_con_cli.list_buckets()['Buckets']:
   print each_bucket['Name']

