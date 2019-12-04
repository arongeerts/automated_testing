import boto3, datetime

f = open('test_output.txt')
folder_key = 'TEST_OUTPUT_' + datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
s3 = boto3.client('s3', endpoint_url='http://localhost:5002')

try:
    s3.create_bucket(ACL='public-read-write',
                     Bucket='mybucket')
except:
    pass

s3.put_object(Bucket='mybucket', Key=folder_key, Body= f)