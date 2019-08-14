#!/bin/python
import boto3,sys
from pprint import pprint
while True:
  session=boto3.session.Session(profile_name="dev_root")
  iam_re=session.resource(service_name="iam")
  for each in range(701,1100):
   try:
     iam_re.create_user(UserName="ixasisiidemo"+str(each))
     if each==509:
        sys.exit()
   except:
      continue
