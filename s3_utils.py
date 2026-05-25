import boto3
import os

from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",

    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),

    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),

    region_name=os.getenv("AWS_REGION")
)

BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")


def upload_file_to_s3(file, filename):

    s3.upload_fileobj(
        file,
        BUCKET_NAME,
        filename
    )

    file_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"

    return file_url