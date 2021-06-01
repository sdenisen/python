from sys import stdout
from collections import defaultdict, deque


class RequestCollector:

    def __init__(self, user_limit, service_limit, duration):
        self.user_limit = user_limit
        self.service_limit = service_limit
        self.duration = duration
        self.dict_users = defaultdict(list)  # key = user_id, value = [request_time1, request_time2, ...]
        self.request_times = list()

    def get_request_status(self, str_request_data):
        request = str_request_data.split(" ")
        request_time = int(request[0])
        user_id = int(request[1])
        expected = request_time - self.duration

        def time_condition(r_time): return r_time >= expected

        for r_time in self.dict_users[user_id]:
            if not time_condition(r_time):
                self.dict_users[user_id].pop(0)
                continue
            break
        if len(self.dict_users[user_id]) >= self.user_limit:
            return 429

        for r_time in self.request_times:
            if not time_condition(r_time):
                self.request_times.pop(0)
                continue
            break

        if len(self.request_times) >= self.service_limit:
            return 503

        # add user to dict:
        self.dict_users[user_id].append(request_time)

        # add time to request times list:
        self.request_times.append(request_time)
        return 200


def main():
    data = input().split(" ")
    user_limit = int(data[0])
    service_limit = int(data[1])
    duration = int(data[2])

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
