from __future__ import print_function


import requests
import sys
def lambda_handler(event, context):
    url="https://balajiws.ddnsfree.com/postback.php"

    for record in event['Records']:
        print ("startprocessing")
        payload=record["body"]
        print(str(payload))
        try:
            response = requests.post(url, data=payload, timeout=2)
            print(response.text)
            print(response.status_code, response.reason)
        except:
            print("Error in requests")
            pass

