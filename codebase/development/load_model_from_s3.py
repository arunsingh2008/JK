



import boto3
import os

def load_model_from_s3(model_file_name, bucket_name):
    # Initialize a session using Amazon S3
    s3 = boto3.client('s3')

    # The name of the local file to save the model
    local_file_name = model_file_name.split('/')[-1]

    # Download the model file from S3 to the local file
    s3.download_file(bucket_name, model_file_name, local_file_name)

    # Return the path to the local model file
    return local_file_name




