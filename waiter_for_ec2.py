#!/usr/bin/python
import boto3
import time
session=boto3.session.Session(profile_name="dev_root")
ec2_re=session.resource(service_name="ec2",region_name="us-east-1")
my_in=ec2_re.Instance(id="i-04d79d94e0415e891")
my_in.start()
my_in.wait_until_running()
