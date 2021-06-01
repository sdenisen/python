import unittest

import task5.task5_resolve


class MyTestCase(unittest.TestCase):
    def test_something(self):
        rc = task5.task5_resolve.RequestCollector(user_limit=3, service_limit=5, duration=0.0001)
        verify_data = [(1, 100, 200), (1, 100, 200), (1, 100, 200), (1, 100, 200), (1, 100, 200)]
        for user_id, request_time, responce in verify_data:
            r = rc.get_request_status(f"{user_id} {request_time}")
        self.assertEqual(r, responce)



if __name__ == '__main__':
    unittest.main()
