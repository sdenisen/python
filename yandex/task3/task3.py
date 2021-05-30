import json

fid_count = input()
l = []
for i in range(int(fid_count)):
    fid = input()
    l.append(json.loads(fid))

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

r = sorted(result, key=lambda item: (item['price'], item['offer_id']))
offers_sorted = {"offers": r}

print(json.dumps(offers_sorted))
