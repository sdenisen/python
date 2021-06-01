from sys import stdout
from collections import defaultdict


class RequestCollector:

    def __init__(self, user_limit, service_limit, duration):
        self.user_limit = user_limit
        self.service_limit = service_limit
        self.duration = duration
        self.user_requests_dict = defaultdict(list)  # {<user_id_1>: [request_time1, request_time2, ...], ...}
        self.service_requests_list = list()

    def get_request_status_for(self, user_id, request_time):

        def is_meet_time_condition(r_time):
            return r_time >= (request_time - self.duration)

        #  check user limit:
        for r_time in self.user_requests_dict[user_id]:
            if is_meet_time_condition(r_time):
                break
            self.user_requests_dict[user_id].pop(0)

        if len(self.user_requests_dict[user_id]) >= self.user_limit:
            return 429

        #  check service limit:
        for r_time in self.service_requests_list:
            if is_meet_time_condition(r_time):
                break
            self.service_requests_list.pop(0)

        if len(self.service_requests_list) >= self.service_limit:
            return 503

        #  update with new request:
        self.user_requests_dict[user_id].append(request_time)
        self.service_requests_list.append(request_time)
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

        request = new_request.split(" ")
        request_time = int(request[0])
        user_id = int(request[1])

        status = rc.get_request_status_for(user_id=user_id, request_time=request_time)
        print(status)
        stdout.flush()


if __name__ == "__main__":
    main()
