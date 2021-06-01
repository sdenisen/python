from urllib import parse
import requests
import json


def handle_cgi_request(url, port, param_a, param_b):
    query_args = {'a': param_a, 'b': param_b}
    encoded_args = parse.urlencode(query_args)
    full_url = f"{url}:{port}?{encoded_args}"
    response_json = requests.get(full_url).text
    arr = json.loads(response_json)
    arr.sort()
    return arr


def main():
    url = input()
    port = input()
    a = input()
    b = input()
    arr = handle_cgi_request(url, port, a, b)
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()
