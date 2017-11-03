import boto3
from botocore.client import Config
import zipfile
import StringIO
import mimetypes

s3 = boto3.resource('s3',config=Config(signature_version='s3v4'))

portfolio_bucket = s3.Bucket('porfolio.halfknown.me.uk')
build_bucket = s3.Bucket('jjbuild.halfknown.me.uk')

porfolio_zip = StringIO.StringIO() 

build_bucket.download_fileobj('jjportbuild.zip', porfolio_zip)

with zipfile.ZipFile(porfolio_zip) as myzip: 
   for nm in myzip.namelist():
       obj = myzip.open(nm)
       portfolio_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]} )
       portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

print "Yeah .. JayJay, Job done !! "
