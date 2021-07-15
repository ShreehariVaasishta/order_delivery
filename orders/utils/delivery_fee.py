from orders.constants import DELIVERY_FEEE_PRICE, LAST_RANGE, INITIAL_RANGE, MAX_FEE


def get_delivery_fee(distance: int) -> int:
    # If the distance is less than the initial range, return the fee for that range
    if distance < INITIAL_RANGE:
        return DELIVERY_FEEE_PRICE[INITIAL_RANGE]

    # if distance is greater than the last range, return the fee for that range
    if distance > LAST_RANGE:
        return DELIVERY_FEEE_PRICE[LAST_RANGE]

    # If the distance is in the range, return the fee for that range
    for distance_range, fee in DELIVERY_FEEE_PRICE.items():
        if distance <= distance_range:
            return fee
    return MAX_FEE
