#!/usr/bin/python
import boto3
import botocore

session = boto3.Session(profile_name='dev')

s3 = session.resource('s3')
my_bucket = 'mys3bucket345435345'
bucket = s3.Bucket(my_bucket)
exists = True
try:
    s3.meta.client.head_bucket(Bucket=my_bucket)
except botocore.exceptions.ClientError as e:
    # If a client error is thrown, then check that it was a 404 error.
    # If it was a 404 error, then the bucket does not exist.
    error_code = int(e.response['Error']['Code'])
    print(error_code)
    if error_code == 404:
        exists = False
except botocore.errorfactory.NoSuchBucket:
    exists = False
finally:
    if exists == False:
        print('Bucket does not exist')
    else:
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()
        print('Bucket deleted')
