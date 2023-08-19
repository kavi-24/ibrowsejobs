import requests

url = "https://judge0-ce.p.rapidapi.com/submissions"

querystring = {"base64_encoded": "true", "fields": "*"}

payload = {
    "language_id": 71,
    "source_code": "print(\"Hello world!\")",
}
headers = {
    "content-type": "application/json",
    "Content-Type": "application/json",
    "X-RapidAPI-Key": "70dc929f10msh5dfa4cee35d2fe2p145b47jsne38d4fce11bc",
    "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
}
response = requests.post(
    url, json=payload, headers=headers, params=querystring)
print(f"POST: {response.json()}")
token = response.json()["token"]


url = f"https://judge0-ce.p.rapidapi.com/submissions/{token}"
querystring = {"base64_encoded": "true", "fields": "*"}
headers = {
    "X-RapidAPI-Key": "70dc929f10msh5dfa4cee35d2fe2p145b47jsne38d4fce11bc",
    "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)
print(response.json())
