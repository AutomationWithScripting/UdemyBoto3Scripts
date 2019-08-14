#!/bin/python
import boto3
from pprint import *
session=boto3.session.Session(profile_name="dev_root")

ec2_client=session.client(service_name="ec2",region_name="us-east-1")

f_bkp={'Name':'tag:Prod','Values':['backup','Backup']}
for each_volume in ec2_client.describe_volumes( Filters=[f_bkp]  )['Volumes']:
   pprint (each_volume)
   break
