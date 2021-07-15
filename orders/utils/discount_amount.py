from typing import Dict, Optional


def get_discount_amount(total_without_discount: int, delivery_fee: int, offer: Optional[Dict] = {}):
    if offer:
        if offer.get("offer_type") == "FLAT":
            return min(total_without_discount, offer.get("offer_val"))

        if offer.get("offer_type") == "DELIVERY":
            return delivery_fee

    return 0
