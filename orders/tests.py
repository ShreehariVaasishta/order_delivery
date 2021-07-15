import re
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
import json

from orders.constants import BASE_JSON_POST_DATA


# Write your tests here.
class TestOrderAmount(TestCase):
    def setUp(self) -> None:
        self.order_post_endpoint = reverse("orders:api:order-calculator")
        self.order_post_payload = BASE_JSON_POST_DATA.copy()
        self.client = APIClient()

    def calculate_amount(self):
        return

    def test_order_value_with_flat_offer(self):
        response = self.client.post(
            self.order_post_endpoint,
            data=json.dumps(self.order_post_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_order_value_with_delivery_offer(self):
        response = self.client.post(
            self.order_post_endpoint,
            data=json.dumps(self.order_post_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
