#!/usr/bin/python3

import boto3
import sys
import botocore

action = sys.argv[1]
bucket_name = sys.argv[2]

session = boto3.Session(profile_name='dev')
s3_client = session.client('s3')

if action == 'create-bucket':
    print('Creating bucket %s' % action)
    s3_client.create_bucket(Bucket=bucket_name)
