#!/bin/python
import boto3

session=boto3.session.Session(profile_name="dev_root")
sts_client=session.client("sts")

print sts_client.get_caller_identity().get('Account')
