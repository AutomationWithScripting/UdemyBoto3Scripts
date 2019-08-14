#!/usr/bin/python
import boto3
session=boto3.session.Session(profile_name="dev_root")
ec2_console_client=session.client(service_name='ec2',region_name='us-east-1')

#print dir(ec2_console_client)

print ec2_console_client.describe_instance_status(InstanceIds=['i-04d79d94e0415e891'])
