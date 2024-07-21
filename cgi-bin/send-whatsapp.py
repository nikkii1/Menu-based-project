#!/usr/bin/env python3

import cgi
import cgitb
import json
import http.client

cgitb.enable()

print("Content-Type: text/html")
print()

try:
    form = cgi.FieldStorage()
    from_number = form.getvalue("from")
    to_number = form.getvalue("to")
    message = form.getvalue("message")

    conn = http.client.HTTPSConnection("qy8643.api.infobip.com")
    payload = json.dumps({
        "messages": [
            {
                "from": from_number,
                "to": to_number,
                "messageId": "f46d294c-4b70-428c-b420-915abd6ab2b4",
                "content": {
                    "templateName": "message_test",
                    "templateData": {
                        "body": {
                            "placeholders": [message]
                        }
                    },
                    "language": "en"
                }
            }
        ]
    })
    headers = {
        'Authorization': 'App aab2c9a6c804861d67cc6db084a87d40-6224efcb-2175-48dd-8894-bef36c06fd34',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    conn.request("POST", "/whatsapp/1/message/template", payload, headers)
    res = conn.getresponse()
    data = res.read()
    response = data.decode("utf-8")

    print(f"<p>Message sent successfully! Server response: {response}</p>")
except Exception as e:
    print(f"<p>Error in sending the message: {e}</p>")
