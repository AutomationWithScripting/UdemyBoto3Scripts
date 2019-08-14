#!/bin/python
import boto3
import datetime

session=boto3.session.Session(profile_name="dev_root")
ec2_res=session.resource(service_name="ec2",region_name="us-east-1")
ec2_cli=session.client(service_name="ec2",region_name="us-east-1")
sts_client=session.client("sts")
ownaccountid=sts_client.get_caller_identity().get('Account')
today=datetime.datetime.now()

start_time=str(datetime.datetime(today.year,today.month,today.day,4,15,44))
print start_time
print "Below is using resource object"
for each_snap in ec2_res.snapshots.filter(OwnerIds=[ownaccountid]):
    if each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S")==start_time:
       print  each_snap.id,each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S")
'''
f_size={'Name':'volume-size','Values':['10']}
print 'Below is using client object'
for each_snap in ec2_cli.describe_snapshots(Filters=[f_size],OwnerIds=[ownaccountid])['Snapshots']:
    print each_snap['SnapshotId']
'''
