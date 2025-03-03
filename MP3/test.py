import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp3-lexv2-autograder"

payload = {
	"graphApi": "https://olfz0tkyed.execute-api.us-east-1.amazonaws.com/test/insertdistance",
	"botId": "LTOVQZSDUG", # <id of your Amazon Lex Bot>, 
	"botAliasId": "EO1LZMFKO9", # <Lex alias id>,
	"identityPoolId": "us-east-1:dd446435-9cad-41c6-8073-c241b5be299f", #<cognito identity pool id for lex>,
	"accountId": "484907523136",
	"submitterEmail": "sgirten2@illinois.edu",
	"secret": "yeaiZ0WNeG7YjD4Q", # <insert your secret token from coursera>,
	"region": "us-east-1"
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)