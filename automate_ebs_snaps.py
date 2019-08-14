#!/bin/python
import boto3
from pprint import pprint

session=boto3.session.Session(profile_name="dev_root")

ec2_client=session.client(service_name="ec2",region_name="us-east-1")
list_of_volids=[]
f_prod_bkp={'Name':'tag:Prod','Values':['backup','Backup']}
#for each_vol in ec2_client.describe_volumes(Filters=[f_prod_bkp])['Volumes']:
#   list_of_volids.append(each_vol['VolumeId'])
paginator = ec2_client.get_paginator('describe_volumes')
for each_page in paginator.paginate(Filters=[f_prod_bkp]):
   for each_vol in each_page['Volumes']:
      list_of_volids.append(each_vol['VolumeId'])



print "The list of volids are: ",list_of_volids
snapids=[]
for each_volid in list_of_volids:
    print "Taking snap of {}".format(each_volid)
    res=ec2_client.create_snapshot( 
             Description="Taking snap with Lambda and cw",
             VolumeId=each_volid,
             TagSpecifications=[
                 {
                    'ResourceType':'snapshot',
                     'Tags': [
                         {
                            'Key': 'Delete-on',
                            'Value': '90'
                         }
                             ]
                 }
                ]
               )
    snapids.append(res.get('SnapshotId'))

print "The snap ids are: ",snapids


waiter = ec2_client.get_waiter('snapshot_completed')
waiter.wait(SnapshotIds=snapids)

print "Succssfully completed snaps for the volumes of {}".format(list_of_volids)


















         
