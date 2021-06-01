import time
from sys import stdout
from collections import defaultdict


def initData():
    data = input().split(" ")
    user_limit = int(data[0])
    service_limit = int(data[1])
    duration = int(data[2])
    return user_limit, service_limit, duration


class RequestCollector:

    def __init__(self, user_limit, service_limit, duration):
        self.user_limit = user_limit
        self.service_limit = service_limit
        self.duration = duration
        self.dict_users = defaultdict(list)  # key = user_id, value = [request_time1, request_time2, ...]
        self.request_times = list()

    def check_timeouts(self, user_id, new_request):
        r = []
        for request_time in self.dict_users[user_id]:
            if request_time < new_request - self.duration:
                continue
            r.append(request_time)
        return r

    def check_request_times(self, new_request):
        r = list()
        for time in self.request_times:
            if time < new_request - self.duration:
                continue
            r.append(time)
        return r

    def get_request_status(self, str_request_data):
        request = str_request_data.split(" ")
        request_time = int(request[0])
        user_id = request[1]

        r = self.check_timeouts(user_id, request_time)
        if len(r) > self.user_limit - 1:
            return 429

        r_service_requests = self.check_request_times(new_request=request_time)
        if len(r_service_requests) > self.service_limit - 1:
            return 503

        # add user to dict:
        r.append(request_time)
        r_service_requests.append(request_time)

        # add time to request times list:
        self.dict_users[user_id] = r
        self.request_times = r_service_requests
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


if __name__ == "__main__":
    main()


