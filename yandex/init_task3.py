import json
fid_count = 2
fid_1 = '{"offers": [{"offer_id": "offer1", "market_sku": 10846332, "price": 499}, ' \
        '{"offer_id": "offer2", "market_sku": 682644, "price": 499}]}'

fid_2 = '{"offers": [{"offer_id": "offer3", "market_sku": 832784, "price": 14000}]}'

fid_3 = '{"offers":[{"market_sku":682644,"offer_id":"offer2","price":499},' \
        '{"market_sku":10846332,"offer_id":"offer1","price":499},' \
        '{"market_sku":832784,"offer_id":"offer3","price":14000}]}'

print(json.loads(fid_1))

{"offers":[{"market_sku":682644,"offer_id":"offer2","price":499},
           {"market_sku":10846332,"offer_id":"offer1","price":1490},
           {"market_sku":832784,"offer_id":"offer3","price":14000}]}

l = [json.loads(fid_1), json.loads(fid_2), json.loads(fid_3)]
result_unique_fids = []

offer_ids = []
for fid in l:
    for offer in fid["offers"]:
        offer_ids.append(offer['offer_id'])
offer_ids = list(set(offer_ids))
offer_ids.sort()

result = []
for offer_id in offer_ids:
    for fid in l:
        for offer in fid['offers']:
            if offer['offer_id'] == offer_id and offer not in result:
                result.append(offer)
print(result)

result.sort(key=lambda item: item['price'] or item['offer_id'])

print(result)
