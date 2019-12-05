import json
import traceback

import boto3, datetime

f = open('test_output.txt')
folder_key = 'TEST_OUTPUT_' + datetime.datetime.now().strftime('%Y-%m-%d') + '.html'
s3 = boto3.client('s3',
                  endpoint_url='http://localstack-s3:5002',
                  aws_access_key_id='foo',
                  aws_secret_access_key='bar')

try:
    s3.create_bucket(ACL='public-read-write',
                     Bucket='mybucket')
except:
    print('bucket mybucket already exists')

body = f.read().split('\n')
print(body)

html = '<html><body><table cellpadding="20"><th>test</th><th>status</th><th>message</th>'

for line in body:
    l = json.loads(line)
    if l == '':
        continue
    html += '<tr><td>{}</td><td>{}</td><td>{}</td></tr>'.format(l['test_name'], l['result'], l.get('error_msg', ''))

html += '</table></body></html>'

s3.put_object(Bucket='mybucket', Key=folder_key, Body=html)

print('object available at http://localhost:5002/mybucket/{}'.format(folder_key))
