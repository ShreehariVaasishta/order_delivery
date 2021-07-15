from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from orders.serializers import OrderSerializer
from orders.utils import get_delivery_fee, get_items_total_cost, get_discount_amount

# Create your views here.


@api_view(["POST"])
def calculate_order(request: Request) -> Response:
    """
    Calculate the order for the given request
    :param request: Request
    :return: Response
    """
    serializer = OrderSerializer(data=request.data)

    # Validate the request data
    if serializer.is_valid(raise_exception=True):
        serialized_data = serializer.data
        items_total = get_items_total_cost(serialized_data.get("order_items"))
        delivery_fee = get_delivery_fee(serialized_data.get("distance"))
        total_without_discount = items_total + delivery_fee
        payable_amount = total_without_discount - get_discount_amount(
            total_without_discount, delivery_fee, serialized_data.get("offer")
        )

        details = {"order_total": payable_amount}

    return Response(details, status=HTTP_200_OK)
