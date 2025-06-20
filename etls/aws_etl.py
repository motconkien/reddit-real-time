from utils.constants import AWS_REGION,AWS_SECRET_KEY,AWS_ID,AWS_BUCKET_NAME
import boto3
from botocore.exceptions import ClientError
import sys

def connect_to_s3():
    try:
        s3=boto3.client(
            's3',
            aws_access_key_id=AWS_ID,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=AWS_REGION
        )
        print(f"Connected S3")
        return s3
    except Exception as e:
        raise Exception("No AWS credentials found. Please check your environment.")
        # sys.exit(1)

def create_bucket(s3):
    try:
        s3.head_bucket(Bucket=AWS_BUCKET_NAME)
        print(f"Bucket '{AWS_BUCKET_NAME}' already exists.")
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            # Bucket does not exist, create 
            print(f"Creating bucket '{AWS_BUCKET_NAME}'...")
            if AWS_REGION:
                s3.create_bucket(
                    Bucket=AWS_BUCKET_NAME,
                    CreateBucketConfiguration={'LocationConstraint': AWS_REGION}
                )
            else:
                s3.create_bucket(Bucket=AWS_BUCKET_NAME)
            print(f"Bucket '{AWS_BUCKET_NAME}' created.")
        else:
            raise

def load_to_s3(s3,filename,key):
    try:
        #Filename (str) – The path to the file to upload.
        s3.upload_file(filename, AWS_BUCKET_NAME, key)
        print('File uploaded to s3')
    except FileNotFoundError:
        print('The file was not found', "\nFile name:", filename, "\nS3_key:", key)