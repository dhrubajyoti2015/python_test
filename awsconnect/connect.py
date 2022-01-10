import boto3

#s3_client = boto3.client('s3')
s3 = boto3.resource(
    service_name='s3',
    region_name='ap-south-1',
    aws_access_key_id='AKIA4EBN7IAIEAVUU4UK',
    aws_secret_access_key='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'
)

for bucket in s3.buckets.all():
    print(bucket.name)

