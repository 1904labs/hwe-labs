import boto3
import os

# Load environment variables.
from dotenv import load_dotenv
load_dotenv()

handle= os.environ.get("AWS_HANDLE")
aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")

# Initialize the S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)


# Define the S3 bucket and file path
bucket_name = 'hwe-fall-2023'
file_key = f'{handle}/success_message'

# Download and display the contents of the S3 object
try:
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    content = response['Body'].read().decode('utf-8')
    print(content)
except Exception as e:
    print(f"Error: {str(e)}")
