import requests

#https://[host]/CuratorGateway/connect/authorize?client_id=0a677a41c5f7491d949c9eb4b1098ab0&redirect_uri=https://myapp.com&response_type=code&grant_type=authorization_code&scope=Curator.Server.API Curator.Gateway.API
url = "https://localhost:54279/CuratorGateway/api/v1"

payload = {}
headers = {
  'Authorization': 'Bearer [access token]'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))