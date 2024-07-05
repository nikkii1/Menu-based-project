#!/usr/bin/env python3

import boto3
import json
import cgi
import cgitb

# Hardcoded AWS credentials (for demo purposes only)
ACCESS_KEY_ID = 'your key'
SECRET_ACCESS_KEY = 'your secret key'

# Enable detailed error messages to be shown in the browser
cgitb.enable()

def create_iam_group(group_name, region):
    try:
        # Initialize a session using hardcoded credentials
        session = boto3.Session(
            aws_access_key_id=ACCESS_KEY_ID,
            aws_secret_access_key=SECRET_ACCESS_KEY,
            region_name=region
        )

        # Initialize IAM client
        iam_client = session.client('iam')

        # Create IAM group
        response = iam_client.create_group(
            GroupName=group_name
        )

        return {"status": "success", "message": f"IAM group '{group_name}' created successfully."}

    except iam_client.exceptions.EntityAlreadyExistsException:
        return {"status": "error", "message": f"IAM group '{group_name}' already exists."}

    except Exception as e:
        return {"status": "error", "message": f"Error creating IAM group: {str(e)}"}

def main():
    # Parse form data
    form = cgi.FieldStorage()
    group_name = form.getvalue('group_name')
    region = form.getvalue('region')

    # Create IAM group
    result = create_iam_group(group_name, region)

    # Return JSON response
    print("Content-Type: application/json")
    print()
    print(json.dumps(result))

if __name__ == "__main__":
    main()
