#!/usr/bin/python3

import boto3
import json
import cgi
import cgitb

# Enable CGI error reporting
cgitb.enable()

# Initialize a session using your credentials
session = boto3.Session(
    aws_access_key_id = "YOUR_ACCESS_KEY",
    aws_secret_access_key = "YOUR_SECRET_KEY",
    region_name='ap-south-1'  # Replace with your desired region
)

# Initialize IAM client
iam_client = session.client('iam')

# Function to create IAM role
def create_iam_role(role_name, assume_role_policy_document):
    try:
        # Create IAM role
        response = iam_client.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(assume_role_policy_document)
        )
        return {'status': 'success', 'message': f"Role '{role_name}' created successfully."}
    except iam_client.exceptions.EntityAlreadyExistsException:
        return {'status': 'error', 'message': f"Role '{role_name}' already exists."}
    except Exception as e:
        return {'status': 'error', 'message': f"Error creating role: {str(e)}"}

# Main CGI handler
def main():
    try:
        # Parse form data
        form = cgi.FieldStorage()
        role_name = form.getvalue('role_name')

        # Role name and policy document
        assume_role_policy_document = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "ec2.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }

        # Create IAM role
        result = create_iam_role(role_name, assume_role_policy_document)

        # Return JSON response
        print("Content-Type: application/json")
        print()
        print(json.dumps(result))

    except Exception as e:
        print("Content-Type: application/json")
        print()
        print(json.dumps({'status': 'error', 'message': str(e)}))

if __name__ == '__main__':
    main()