#!/usr/bin/env python3

import cgi
import cgitb
import json

cgitb.enable()  # Enable debugging

def main():
    print("Content-Type: application/json")
    print()  # End of headers

    # List of 10 curl commands
    curl_commands = [
        "curl -X GET https://api.example.com/resource",
        "curl -X POST https://api.example.com/resource -d '{\"key\":\"value\"}'",
        "curl -X PUT https://api.example.com/resource/1 -d '{\"key\":\"new_value\"}'",
        "curl -X DELETE https://api.example.com/resource/1",
        "curl -X PATCH https://api.example.com/resource/1 -d '{\"key\":\"patched_value\"}'",
        "curl -I https://api.example.com/resource",
        "curl -L https://api.example.com/resource",
        "curl -O https://api.example.com/resource/file.txt",
        "curl -u user:password https://api.example.com/resource",
        "curl -H 'Authorization: Bearer <token>' https://api.example.com/resource"
    ]

    response = {"curl_commands": curl_commands}
    print(json.dumps(response))

if __name__ == "__main__":
    main()
