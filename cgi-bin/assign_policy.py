#!/usr/bin/env python3

import cgi
import cgitb
import json
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
import os

cgitb.enable()  # Enable debugging

def main():
    print("Content-Type: application/json")
    print()  # End of headers

    form = cgi.FieldStorage()

    user_name = form.getvalue('user_name')

    # Define AWS credentials and region (ideally, these should be set via environment variables)
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID', 'your key')
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY', 'your secret key')
    region_name = os.environ.get('AWS_REGION', 'ap-south-1')

    policy_arn = 'arn:aws:iam::aws:policy/AmazonEC2FullAccess'

    if not user_name:
        response = {"error": "User name is required"}
        print(json.dumps(response))
        return

    try:
        session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )

        iam = session.client('iam')

        iam.attach_user_policy(
            UserName=user_name,
            PolicyArn=policy_arn
        )

        response = {"message": f"Policy {policy_arn} has been successfully attached to user {user_name}."}
        print(json.dumps(response))

    except (NoCredentialsError, PartialCredentialsError):
        response = {"error": "Invalid AWS credentials"}
        print(json.dumps(response))

    except ClientError as e:
        response = {"error": str(e)}
        print(json.dumps(response))

    except Exception as e:
        response = {"error": str(e)}
        print(json.dumps(response))

if __name__ == "__main__":
    main()
