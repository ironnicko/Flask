import requests
import json
url = "https://genius.p.rapidapi.com/search"
artist = input("Enter the artists name")
querystr = {"id": artist}
headers = {
    "x-rapidapi-key": "ce19d0164fmsh3d383efc0e85ce5p16dcb1jsnb1a4a3c79541",
    "x-rapidapi-host": "genius.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers, params=querystr)
json_data = json.loads(response.text)
