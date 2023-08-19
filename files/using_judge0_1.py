import requests

url = "https://judge0-ce.p.rapidapi.com/about"

headers = {
	"X-RapidAPI-Key": "70dc929f10msh5dfa4cee35d2fe2p145b47jsne38d4fce11bc",
	"X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())