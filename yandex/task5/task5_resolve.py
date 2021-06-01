import time
from sys import stdout
from collections import defaultdict


def initData():
    data = input().split(" ")
    user_limit = int(data[0])
    service_limit = int(data[1])
    duration = float(data[2]) / 1000
    return user_limit, service_limit, duration


class RequestCollector:

    def __init__(self, user_limit, service_limit, duration):
        self.user_limit = user_limit
        self.service_limit = service_limit
        self.duration = duration
        self.dict_users = defaultdict(list)  # key = user_id, value = [request_time1, request_time2, ...]
        self.count_service_requests = 0

    def check_timeouts(self, user_requests_time, duration, src):
        r = []
        for request_time in user_requests_time:
            if request_time < time.time() - duration:
                src -= 1
                continue
            r.append(request_time)
        return r, src

    def get_request_status(self, str_request_data):
        request = str_request_data.split(" ")
        user_id = request[1]
        request_time = int(request[0])

        user_requests = self.dict_users[user_id]
        result, count = self.check_timeouts(user_requests, self.duration, self.count_service_requests)
        count_service_requests = count
        if len(result) > self.user_limit - 1:
            return 429

        if count_service_requests > self.service_limit - 1:
            return 503

        # add user to dict:
        result.append(request_time)
        self.dict_users[user_id] = result
        count_service_requests += 1
        return 200


def main():

    user_limit, service_limit, duration = initData()

    rc = RequestCollector(user_limit, service_limit, duration)

    while True:
        new_request = input()
        if new_request == "-1":
            break
        status = rc.get_request_status(str_request_data=new_request)
        print(status)
        stdout.flush()

print(__file__)
print(__name__)
if __name__ == "__main__":
    main()


