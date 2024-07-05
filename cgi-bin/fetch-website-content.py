#!/usr/bin/env python3

import cgi
import cgitb
import json
import requests
from bs4 import BeautifulSoup

cgitb.enable()  # Enable debugging

def print_website_content(url):
    try:
        # Fetch the content of the website
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Target the specific element containing the main content
        content_div = soup.find(id="bodyContent")

        # Extract and return the text content
        if content_div:
            return content_div.get_text()
        else:
            return "Main content not found."

    except requests.exceptions.RequestException as e:
        return f"Error fetching the website: {e}"

def main():
    print("Content-Type: application/json")
    print()  # End of headers

    form = cgi.FieldStorage()
    url = form.getvalue('url')

    if not url:
        response = {"error": "URL is required"}
        print(json.dumps(response))
        return

    content = print_website_content(url)
    response = {"content": content}
    print(json.dumps(response))

if __name__ == "__main__":
    main()
