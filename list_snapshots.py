#!/bin/python
import boto3
from botocore.exceptions import ClientError

session=boto3.session.Session(profile_name="dev_root")
sts_cli=session.client("sts")
print sts_cli.get_caller_identity()

'''
ec2_re=session.resource(service_name="ec2",region_name="us-east-1")
cnt=1
for each_snap in ec2_re.snapshots.filter(OwnerIds=["943637252859"]):
    print cnt,each_snap
    cnt+=1
'''
