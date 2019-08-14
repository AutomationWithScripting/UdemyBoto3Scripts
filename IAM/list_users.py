import boto3
iam_re=boto3.session.Session(profile_name="dev_root").resource('iam')
iam_cli=boto3.session.Session(profile_name="dev_root").client('iam')
cnt=1
'''
for each in iam_re.users.all():
  print cnt,each.user_name
  cnt=cnt+1
for each in iam_cli.list_users()['Users']:
   print each

print len(iam_cli.list_users()['Users'])
'''

paginator = iam_cli.get_paginator('list_users')
for each_page in paginator.paginate(PathPrefix="/"):
    print len( each_page['Users'])
