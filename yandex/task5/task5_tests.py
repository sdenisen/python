import time
import unittest

import task5.task5_resolve


class MyTestCase(unittest.TestCase):
    def test_something(self):
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
            r = rc.get_request_status(f"{request_time} {user_id}")
            print(f"user_id: {user_id} request_time: {request_time} -> response: {r}; {i} -> {rc.dict_users} ===> {rc.request_times}")
            i += 1
            self.assertEqual(r, responce)
            # print(rc.dict_users)




if __name__ == '__main__':
    unittest.main()
