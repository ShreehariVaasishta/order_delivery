from rest_framework import serializers

from orders.constants import OFFER_TYPE_LIST


class InlineOrderItemSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    quantity = serializers.IntegerField(required=True)
    price = serializers.IntegerField(required=True)


class InlineOfferSerializer(serializers.Serializer):
    offer_type = serializers.CharField(required=True)
    offer_val = serializers.IntegerField(required=False)

    def validate_offer_type(self, value):
        if value not in OFFER_TYPE_LIST:
            raise serializers.ValidationError("Offer type can be FLAT or DELIVERY")
        return value

    def validate(self, data):
        if data["offer_type"] == "FLAT" and not data.get("offer_val"):
            raise serializers.ValidationError("Offer value can not be null for FLAT offer")
        return data


class OrderSerializer(serializers.Serializer):
    order_items = serializers.ListField(child=InlineOrderItemSerializer(required=True))
    distance = serializers.IntegerField(min_value=0, max_value=500000, required=True)
    offer = InlineOfferSerializer(required=False)
