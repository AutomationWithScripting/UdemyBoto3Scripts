#!/usr/bin/python
import boto3
session=boto3.session.Session(profile_name="dev_root")
ec2_con_re=session.resource(service_name="ec2",region_name="us-east-1")
while True:
  print "This script will perform the following actions on given instance id"
  print "1. start"
  print "2. stop"
  print "3. reboot"
  print "4. terminate"
  print "5. Exit"
  option=input("Enter your action by selecting a number between 1-5: ")
  if option==1:
     in_id=raw_input("Enter your instance id: ")
     my_in=ec2_con_re.Instance(id=in_id)
     print "Please wait we are starting instance"
     my_in.start()
  elif option==2:
     in_id=raw_input("Enter your instance id: ")
     my_in=ec2_con_re.Instance(id=in_id)
     print "Please wait we are stopping instance"
     my_in.stop()
  elif option==3:
     in_id=raw_input("Enter your instance id: ")
     my_in=ec2_con_re.Instance(id=in_id)
     print "Please wait we rebooting instance"
     my_in.reboot()
  elif option==4:
     in_id=raw_input("Enter your instance id: ")
     my_in=ec2_con_re.Instance(id=in_id)
     print "Please wait we are terminating instance"
     my_in.terminate()
  elif option==5:
     print "Thank you for using this script"
     break
  else:
     print "Inavlid option\nPlease select between 1-5"


