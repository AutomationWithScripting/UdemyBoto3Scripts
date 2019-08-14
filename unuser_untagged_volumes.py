#!/usr/bin/python
import boto3
session=boto3.session.Session(profile_name="dev_root")
ec2_con=session.resource("ec2",'us-east-1')
f1={'Name':'status','Values':['available']}
for each_vol in ec2_con.volumes.filter(Filters=[f1]):
   print each_vol.state,each_vol.tags,each_vol.id
