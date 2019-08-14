#!/usr/bin/python
import boto3
import pprint
session=boto3.session.Session(profile_name="dev_root")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=session.client(service_name="ec2",region_name="us-east-1")
#--------------------------
print "Below is using resource object"
for each_in in ec2_con_re.instances.all():     
    print each_in.instance_id, each_in.instance_type
print "Below is using client object"
#pprint.pprint( ec2_con_cli.describe_instances()['Reservations'])
for each_info in ec2_con_cli.describe_instances()['Reservations']:
   for each_inst in each_info['Instances']:
       print each_inst['InstanceId'], each_inst['InstanceType']
