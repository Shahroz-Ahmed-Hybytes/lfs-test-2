#!/usr/bin/env python

import os
import boto3
from botocore.exceptions import NoCredentialsError

def download_all_folders_from_s3(bucket_name, local_base_path):
    """
    Download all folders and their contents from an S3 bucket to the local directory.
    """
    s3 = boto3.client('s3')

    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        objects = response.get('Contents', [])

        if not objects:
            print(f"No objects found in the S3 bucket: {bucket_name}")
            return

        for obj in objects:
            key = obj['Key']

            # Skip objects that represent folders (prefix ends with '/')
            if key.endswith('/'):
                continue

            local_path = os.path.join(local_base_path, key)

            if not os.path.exists(os.path.dirname(local_path)):
                os.makedirs(os.path.dirname(local_path))

            s3.download_file(bucket_name, key, local_path)
            print(f"Downloaded: {key}")

        print("Download completed successfully.")

    except NoCredentialsError:
        print("Credentials not available or incorrect.")

if __name__ == "__main__":
    # Specify your S3 bucket name and local base directory
    s3_bucket_name = "s3testpush"
    local_base_directory = os.path.dirname(os.path.abspath(__file__))

    download_all_folders_from_s3(s3_bucket_name, local_base_directory)
