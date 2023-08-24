# import requests
# import json

# url = "http://localhost:8000/api/auth/convert-token/"

# data = {
#     "token": "4/0Adeu5BVqZZxMiLP3dULuKF8sOyhbJ9AyzDAkTXVGeekqtGoKmATpCJUji6t7uFw0SuYYUA",
#     "backend": "google-oauth2",
#     "grant_type": "convert_token",
#     "client_id": "RtjcxZys5qxL46B9bjPBf4NP1vCpN5wnYrbL0pfb",
#     "client_secret": "pbkdf2_sha256$600000$FxOw5fps9iSqoT6CMmjHb9$zqdRT280aEGS0QEBCbBhgG1Wsl9HVJmmV9CPXZ+/jpQ="
# }

# headers = {
#     "Content-Type": "application/json"  # Set the correct content type
# }

# response = requests.post(url, data=json.dumps(data), headers=headers)

# print(response.text)

import requests

access_token = "GC7qHPvf5cwle2jjb8etGm1RNy533z"
headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get("http://localhost:8000/api/scan/2207/", headers=headers)
print(response.text)
