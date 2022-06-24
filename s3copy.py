import boto3 
import os 
from dotenv import load_dotenv

load_dotenv() # this loads the .env file with our credentials

file_name = 's3.png' # name of the file to upload
bucket_name = 'digitalshelf-source-data' # name of the bucket
dest_file_name = f'test/{file_name}'

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

response = s3_client.upload_file(file_name, bucket_name, dest_file_name)
