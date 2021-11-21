# THIS IS THE URL's that is for our specific app
from django.urls import path

# This is accessing the views/funcitons that we wrote on views.py!!
from .views import findOrdersPageView, searchOrdersPageView
from .views import EditOrderPageView
from .views import AcceptOrderPageView
from .views import storeTicketPageView
from .views import TicketsSummaryView


# we create the path with this syntax
urlpatterns = [

    path("searchorder/", searchOrdersPageView, name="searchorder"),
    path("findorder/", findOrdersPageView, name='findorder'),
    path("editorder/", EditOrderPageView, name="editorder"),
    path("acceptorder/", AcceptOrderPageView, name="acceptorder"),
    path("storeticket/", storeTicketPageView, name="storeticket"),
    path("ticketsummary/", TicketsSummaryView, name="ticketsummary"),

]
