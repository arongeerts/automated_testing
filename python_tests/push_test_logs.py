import boto3, datetime

f = open('test_output.txt')
folder_key = 'TEST_OUTPUT_' + datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
s3 = boto3.client('s3',
                  endpoint_url='http://localstack-s3:5002',
                  aws_access_key_id='foo',
                  aws_secret_access_key='bar')

try:
    s3.create_bucket(ACL='public-read-write',
                     Bucket='mybucket')
    print('created bucket mybucket')
except:
    print('bucket mybucket already exists')


s3.put_object(Bucket='mybucket', Key=folder_key, Body=f)
