from typing import List


def get_items_total_cost(order_items: List[dict]) -> int:
    price_list = [order["price"] * order["quantity"] for order in order_items]
    return sum(price_list)
