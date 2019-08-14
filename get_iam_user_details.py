#!/bin/python
import boto3
import pprint
session=boto3.session.Session(profile_name="dev_root")
re_iam=session.resource(service_name="iam",region_name="us-east-1")
iam_user_ob=re_iam.User("EC2_S3_IAM")

pprint.pprint(dir(iam_user_ob))
print "IAM Deatials"
print "============"
print "UserName:{}\nUserId:{}\nUserARN:{}\nUserCreationDate:{}".format(iam_user_ob.user_name,iam_user_ob.user_id,iam_user_ob.arn,iam_user_ob.create_date)
