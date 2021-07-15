OFFER_TYPE_LIST = ["FLAT", "DELIVERY"]

INITIAL_RANGE = 10000
LAST_RANGE = 50000
MAX_FEE = 100000

DELIVERY_FEEE_PRICE = {
    # distance_range(in meters): price(in paisa)
    INITIAL_RANGE: 5000,
    20000: 1000,
    LAST_RANGE: 5000,
}

BASE_JSON_POST_DATA = {
    "order_items": [{"name": "bread", "quantity": 2, "price": 2200}, {"name": "butter", "quantity": 1, "price": 5900}],
    "distance": 1200,
    "offer": {"offer_type": "FLAT", "offer_val": 1000},
}
