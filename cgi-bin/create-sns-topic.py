#!/usr/bin/env python3

import boto3
import json
import cgi
import cgitb

# Enable detailed error messages to be shown in the browser
cgitb.enable()

def create_sns_topic(topic_name, region, access_key_id, secret_access_key):
    try:
        # Initialize a session using your credentials
        session = boto3.Session(
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            region_name=region
        )

        # Initialize SNS client
        sns_client = session.client('sns')

        # Create SNS topic
        response = sns_client.create_topic(
            Name=topic_name
        )

        topic_arn = response['TopicArn']
        return {"status": "success", "message": f"SNS topic '{topic_name}' created successfully with ARN: {topic_arn}"}

    except Exception as e:
        return {"status": "error", "message": f"Error creating SNS topic: {str(e)}"}

def main():
    # Parse form data
    form = cgi.FieldStorage()
    topic_name = form.getvalue('topic_name')
    region = form.getvalue('region')
    aws_access_key_id = 'AKIARBK7BRBVRR56TL7E'  # Hardcoded for demo, secure handling in prod
    aws_secret_access_key = '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'  # Hardcoded for demo, secure handling in prod

    # Create SNS topic
    result = create_sns_topic(topic_name, region, aws_access_key_id, aws_secret_access_key)

    # Return JSON response
    print("Content-Type: application/json")
    print()
    print(json.dumps(result))

if __name__ == "__main__":
    main()
