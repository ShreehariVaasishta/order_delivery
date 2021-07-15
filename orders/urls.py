from django.urls import path, include
from orders import views

app_name = "orders"

urlpatterns = [
    # API URLS
    path(
        "api/",
        include(
            (
                [
                    # Order amount calculator api
                    path(
                        "calculate-order/",
                        views.calculate_order,
                        name="order-calculator",
                    ),
                ],
                app_name,
            ),
            namespace="api",
        ),
    ),
    # Template and Other URLs
]
