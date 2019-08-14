#!/bin/python
import boto3

session=boto3.session.Session(profile_name="dev_root")
'''
iam_re=session.resource("iam")
cnt=1
for each_user in iam_re.users.all():
   print cnt,each_user.user_name
   cnt=cnt+1

cnt=1
iam_cli=session.client("iam")
for each_user in iam_cli.list_users()['Users']:
    print cnt, each_user['UserName']
    cnt=cnt+1
'''

'''
cnt=1
iam_cli=session.client("iam")
paginator = iam_cli.get_paginator('list_users')
for each_page in  paginator.paginate():
    for each_user in     each_page['Users']:
       print cnt,each_user['UserName']
       cnt=cnt+1
'''
iam_cli=session.client("ec2")
paginatro=iam_cli.get_paginator('describe_instances')
for each_page in paginatro.paginate():
     print each_page


