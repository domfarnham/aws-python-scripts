#!/usr/bin/python3
import boto3

# Any clients created from this session will use credentials
# from the [dev] section of ~/.aws/credentials.
session = boto3.Session(profile_name='dev')

s3 = session.resource('s3')
s3.create_bucket(Bucket='mys3bucket345435345')
