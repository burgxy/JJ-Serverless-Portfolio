import boto3 

s3 = boto3.resource('s3') 

portfolio_bucket = s3.Bucket('porfolio.halfknown.me.uk')

for obj in portfolio_bucket.objects.all():
     print obj.key

