import requests

# Replace with your actual values
key = "GHsqlZLUzmNX1CDk2h2BhHgR0uQOXrd0JWXPsFsbvdOQiK71YsqDJQQJ99BIACGhslBXJ3w3AAAbACOG93ZN"
endpoint = "https://api.cognitive.microsofttranslator.com/"
location = "centralindia"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'to': ['fr']  # translate into French
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json'
}

body = [{
    'text': 'Hello Azure Students! This is SaaS in action - SHRUTHI.'
}]

response = requests.post(constructed_url, params=params, headers=headers, json=body)
print(response.json())
