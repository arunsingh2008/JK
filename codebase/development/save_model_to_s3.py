



import boto3


def save_model_to_s3(model_file_path, bucket_name):
    # Initialize a session using Amazon S3
    s3 = boto3.client('s3')

    # Extract the file name from the model file path
    file_name = model_file_path.split('/')[-1]

    try:
        # Upload the model file to the specified bucket
        s3.upload_file(model_file_path, bucket_name, file_name)
        return {'status': 'success', 'message': f'Model {file_name} uploaded successfully to {bucket_name}.'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}



