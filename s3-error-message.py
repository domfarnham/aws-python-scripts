#!/usr/bin/python
import boto3

s3 = boto3.client('s3')

# Will return a ClientError exception "NoSuchBucket"
s3.delete_bucket(Bucket='bucket-that-does-not-exist')

# Will return a ClientErro exception "BucketNotEmpty"
s3.delete_bucket(Bucket='bucket-that-does-exist-with-objects')
