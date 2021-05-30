import time
from sys import stdout
from collections import defaultdict


def check_timeouts(user_requests_time, duration, src):
    r = []
    for request_time in user_requests_time:
        if request_time < time.time() - duration:
            src -= 1
            continue
        r.append(request_time)
    return r, src


data = input().split(" ")
user_limit = int(data[0])
service_limit = int(data[1])
duration = float(data[2])/1000

dict_users = defaultdict(list)  # key = user_id, value = count user requests [end_duration_1, ....]
service_request_count = 0

while True:
    data = input()
    if data == "-1":
        break

    new_request = data.split(" ")
    user_id = new_request[1]
    request_time = int(new_request[0])

    user_requests = dict_users[user_id]
    result, count = check_timeouts(user_requests, duration, service_request_count)
    service_request_count = count
    if len(result) > user_limit - 1:
        print(429)
        stdout.flush()
        continue

    if service_request_count > service_limit - 1:
        print(503)
        stdout.flush()
        continue

    # add user to dict:
    result.append(request_time)
    dict_users[user_id] = result
    service_request_count += 1
    print(200)
    stdout.flush()




