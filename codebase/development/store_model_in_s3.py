

import boto3
import os

# Initialize a session using Amazon S3
s3 = boto3.client('s3')

# Your bucket name
bucket_name = 'your-bucket-name'

# Your model directory
model_directory = 'path/to/your/model'

# Function to upload files to S3
def upload_files(bucket_name, model_directory):
    for root, dirs, files in os.walk(model_directory):
        for file in files:
            local_path = os.path.join(root, file)
            s3_path = os.path.relpath(local_path, model_directory)
            s3.upload_file(local_path, bucket_name, s3_path)
            print(f'{file} has been uploaded to {bucket_name}/{s3_path}')

# Function to set access permissions
def set_access_permissions(bucket_name):
    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'AddPerm',
            'Effect': 'Allow',
            'Principal': '*',
            'Action': ['s3:GetObject'],
            'Resource': f'arn:aws:s3:::{bucket_name}/*'
        }]
    }

    # Convert the policy to a JSON string
    bucket_policy = json.dumps(bucket_policy)
    # Set the new policy on the given bucket
    s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
    print('Access permissions have been set.')

# Main function to store model in S3
if __name__ == '__main__':
    upload_files(bucket_name, model_directory)
    set_access_permissions(bucket_name)


