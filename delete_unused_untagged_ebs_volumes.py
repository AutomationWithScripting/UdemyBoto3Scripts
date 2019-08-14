import boto3
session=boto3.session.Session(profile_name="dev_root")
ec2_re=session.resource(service_name='ec2',region_name='us-east-1')

ec2_cli=session.client(service_name='ec2',region_name='us-east-1')
all_required_volume_ids=[]
#List all ebs volumes:
#febsu={'Name':'status','Values':['available']}
#for each_vol in ec2_re.volumes.filter(Filters=[febsu]):
for each_vol in ec2_re.volumes.all():
   if each_vol.state=="available" and each_vol.tags==None:
      print each_vol.id, each_vol.state, each_vol.tags
      all_required_volume_ids.append(each_vol.id)

#Delete volumes:

for each_vol in all_required_volume_ids:
    volume_ob=ec2_re.Volume(each_vol)
    #print dir(volume_ob)
    print "Deleting volume of id ",each_vol
    volume_ob.delete()

waiter = ec2_cli.get_waiter('volume_deleted')
try:
   waiter.wait(VolumeIds=all_required_volume_ids)
   print "Succsffuly deleted all your volumes which are unused and untagged EBS Volumes"
except Exception as e:
   print e



