import functools
import random
import string
import unittest
from timeit import Timer

from task3.task3_resolve import get_unique_offers


class MyTestCase(unittest.TestCase):
    def test_something(self):
        fid_1 = {"offers": [{"offer_id": "offer1", "market_sku": 10846332, "price": 1490},
                            {"offer_id": "offer2", "market_sku": 682644, "price": 499}]}
        fid_2 = {"offers": [{"offer_id": "offer3", "market_sku": 832784, "price": 14000}]}

        expected_offers = {"offers": [{"market_sku": 682644, "offer_id": "offer2", "price": 499},
                                      {"market_sku": 10846332, "offer_id": "offer1", "price": 1490},
                                      {"market_sku": 832784, "offer_id": "offer3", "price": 14000},
                                      ]}

        input_data = [fid_1, fid_2]
        sorted_offers = get_unique_offers(input_data)
        self.assertDictEqual(expected_offers, sorted_offers)

    def test_big_data(self):
        n = 200
        count_fid = 2000
        input_data = []
        # fid_template = {"offer_id": "str", "market_sku": 555, "price": 444}
        for i in range(n):
            fid = []
            for j in range(count_fid):
                offer_id = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=9))
                market_sku = random.randint(1, 30)
                price = random.randint(1, 30)
                fid_template = {"offer_id": offer_id, "market_sku": market_sku, "price": price}
                fid.append(fid_template)
            input_data.append({"offers": fid})
        print("start time test:")
        t = Timer(functools.partial(get_unique_offers, input_data), globals=globals())

        print(t.timeit(1)/1)


if __name__ == '__main__':
    unittest.main()
