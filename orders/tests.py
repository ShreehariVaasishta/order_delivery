import re
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
import json


# Write your tests here.
class TestOrderAmount(TestCase):
    def setUp(self) -> None:
        self.order_post_endpoint = reverse("orders:api:order-calculator")
        self.client = APIClient()

    def test_order_value_with_flat_offer_1(self):
        payload = {
            "order_items": [
                {"name": "bread", "quantity": 2, "price": 2200},
                {"name": "butter", "quantity": 1, "price": 5900},
            ],
            "distance": 1200,
            "offer": {"offer_type": "FLAT", "offer_val": 1000},
        }
        response = self.client.post(
            self.order_post_endpoint,
            data=json.dumps(payload),
            content_type="application/json",
        )
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_order_value_with_delivery_offer_1(self):
        payload = {
            "order_items": [
                {"name": "bread", "quantity": 2, "price": 2200},
                {"name": "butter", "quantity": 1, "price": 5900},
            ],
            "distance": 1200,
            "offer": {"offer_type": "DELIVERY"},
        }

        response = self.client.post(
            self.order_post_endpoint,
            data=json.dumps(payload),
            content_type="application/json",
        )
        print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_order_value_without_offer_1(self):
        payload = {
            "order_items": [
                {"name": "bread", "quantity": 2, "price": 2200},
                {"name": "butter", "quantity": 1, "price": 5900},
            ],
            "distance": 1200,
        }
        response = self.client.post(
            self.order_post_endpoint,
            data=json.dumps(payload),
            content_type="application/json",
        )
        print(response.json())
        self.assertEqual(response.status_code, 200)
