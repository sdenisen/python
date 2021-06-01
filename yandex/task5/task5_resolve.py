from sys import stdout
from collections import defaultdict


class RequestCollector:

    def __init__(self, user_limit, service_limit, duration):
        self.user_limit = user_limit
        self.service_limit = service_limit
        self.duration = duration
        self.dict_users = defaultdict(list)  # key = user_id, value = [request_time1, request_time2, ...]
        self.request_times = list()

    def check_timeouts(self, user_id, new_request):
        self.dict_users[user_id] = list(
            filter(lambda r_time: r_time >= new_request - self.duration, self.dict_users[user_id])
        )

    def check_request_times(self, new_request):
        self.request_times = list(
            filter(lambda r_time: r_time >= new_request - self.duration, self.request_times)
        )

    def get_request_status(self, str_request_data):
        request = str_request_data.split(" ")
        request_time = int(request[0])
        user_id = request[1]

        def time_condition(r_time): return r_time >= request_time - self.duration

        self.dict_users[user_id] = list(filter(time_condition, self.dict_users[user_id]))

        if len(self.dict_users[user_id]) >= self.user_limit:
            return 429

        self.request_times = list(filter(time_condition, self.request_times))
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
