
from s3_config import s3_resource, AWS_STORAGE_BUCKET_NAME

def test_model_access(model_s3_key):
    """Tests access to the LLAMA3 model stored in AWS S3."""
    try:
        s3_object = s3_resource.Object(AWS_STORAGE_BUCKET_NAME, model_s3_key)
        s3_object.load()
        print(f'Successfully accessed {model_s3_key} in {AWS_STORAGE_BUCKET_NAME}')
        return True
    except Exception as e:
        print(f'Failed to access {model_s3_key} in {AWS_STORAGE_BUCKET_NAME}. Error: {e}')
        return False

# Example usage
# test_model_access('models/llama3_model.bin')
