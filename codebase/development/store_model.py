


from aws_s3_config import upload_file_to_s3, AWS_STORAGE_BUCKET_NAME

MODEL_FILE_NAME = 'llama3_model.bin'

# Assuming the model is saved in the current directory under the name 'llama3_model.bin'
def store_model_in_s3():
    upload_file_to_s3(MODEL_FILE_NAME, AWS_STORAGE_BUCKET_NAME, 'models/llama3_model.bin')
    print('Model successfully stored in S3')

if __name__ == '__main__':
    store_model_in_s3()



