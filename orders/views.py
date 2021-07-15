from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.
@api_view(["POST"])
def calculate_order(request: Request) -> Response:
    """
    Calculate the order for the given request
    :param request: Request
    :return: Response
    """
    details = {"order_total": 123}
    return Response(details)
