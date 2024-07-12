import requests

url = "http://192.168.1.69:8000/splunk/search"
payload = {
    "query": "search index=sysmon EventCode=5 | table _time  User EventCode Image",
    "earliest_time": "-24h",
    "latest_time": "now"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    print("Search Results:", response.json())
else:
    print("Failed to retrieve search results:", response.status_code, response.text)
