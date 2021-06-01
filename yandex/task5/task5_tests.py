import random
import unittest

import task5.task5_resolve


class MyTestCase(unittest.TestCase):

    def test_check_test_data_from_task_description(self):
        rc = task5.task5_resolve.RequestCollector(user_limit=2, service_limit=5, duration=5)

        verify_data = [(1, 100, 200),  # 1
                       (1, 100, 200),  # 2
                       (2, 100, 429),  # 3
                       (2, 200, 200),  # 4
                       (2, 300, 200),  # 5
                       (2, 400, 200),  # 6
                       (2, 500, 503),  # 7
                       (3, 500, 503),  # 8
                       (5, 200, 503),  # 9
                       (6, 100, 429),  # 10
                       (7, 200, 200)]  # 11
        i = 1
        for request_time, user_id, responce in verify_data:
            print(i)
            r = rc.get_request_status(f"{request_time} {user_id}")
            self.assertEqual(r, responce)
            i += 1

    def test2(self):
        # generate big test data:
        limit = 150000
        user_ids = [random.randint(1, 100) for _ in range(limit)]
        request_times = [random.randint(1, 50000) for _ in range(limit)]
        sorted(request_times)
        print("start")
        rc = task5.task5_resolve.RequestCollector(user_limit=50000, service_limit=50000, duration=500)
        res = list()
        for request_time, user_id in zip(request_times, user_ids):
            r = rc.get_request_status(f"{request_time} {user_id}")
            res.append(r)

        print(len(res))



if __name__ == '__main__':
    unittest.main()
