#!/bin/python
import boto3
from pprint import pprint

session=boto3.session.Session(profile_name="dev_root")
ec2_re=session.resource(service_name="ec2",region_name="us-east-1")
vol_ids=[]
#colleting volume Ids
for each_vol in ec2_re.volumes.filter(Filters=[]):
     #print each_vol.id
     vol_ids.append(each_vol.id)

print 'All volume ids are: ',vol_ids

#Creating snapshots for volumes one by one
snap_ids=[]
for each_vo_id in vol_ids:
   response= ec2_re.create_snapshot(
    Description='Snap with Lambda',
    VolumeId=each_vo_id,
    TagSpecifications=[
           {
            'ResourceType': 'snapshot',
             'Tags': [
                {
                    'Key': 'Delete-on',
                    'Value':'90'
                 }
                      ]
          }
       ]
     )
   snap_ids.append(response.id)

print snap_ids
#Creating waiter using client 
ec2_cli=session.client(service_name="ec2",region_name="us-east-1")
waiter = ec2_cli.get_waiter('snapshot_completed')
waiter.wait(SnapshotIds=snap_ids)




