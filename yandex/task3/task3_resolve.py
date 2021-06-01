import json


def get_unique_offers2(fid_list):
    result = []
    unique_offers = set()
    for fid in fid_list:
        for offer in fid['offers']:
            if offer['offer_id'] not in unique_offers:
                result.append(offer)
                unique_offers.add(offer['offer_id'])

    offers = sorted(result, key=lambda item: (item['price'], item['offer_id']))
    return {"offers": offers}


def main():
    count = input()
    fid_list = []
    for _ in range(int(count)):
        offers = input()
        fid_list.append(json.loads(offers))

    sorted_unique_offers = get_unique_offers2(fid_list)
    print(json.dumps(sorted_unique_offers))


if __name__ == "__main__":
    main()
