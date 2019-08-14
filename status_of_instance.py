#!/usr/bin/python
import boto3
session=boto3.session.Session(profile_name="dev_root")
ec2_console_resource=session.resource(service_name="ec2",region_name="us-east-1")
#print dir(ec2_console_resource)
instance_id=raw_input("Enter your instance id to the status: ")
my_instance=ec2_console_resource.Instance(id=instance_id)
print my_instance.state['Name']
