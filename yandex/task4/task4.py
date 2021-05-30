from urllib import parse
import requests
import json

url = "http://127.0.0.1"
port = 7777
a = 2
b = 4
query_args = {'a': a, 'b': b}
encoded_args = parse.urlencode(query_args)
full_url = f"{url}:{port}?{encoded_args}"
response_json = requests.get(full_url).text
arr = json.loads(response_json)
arr.sort()
for i in arr:
    print(i)

