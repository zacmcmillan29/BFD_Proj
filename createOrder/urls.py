# THIS IS THE URL's that is for our specific app
from django.urls import path

# This is accessing the views/funcitons that we wrote on views.py!!
from .views import orderPageView, storeOrderPageView, OrdersSummaryView


# we create the path with this syntax
urlpatterns = [
    path("createorder/", orderPageView, name="orders"),
    path("storeorder/", storeOrderPageView, name='storeorder'),
    path("order/", OrdersSummaryView, name="orders"),
    path("orders/", OrdersSummaryView, name="orders")

]
