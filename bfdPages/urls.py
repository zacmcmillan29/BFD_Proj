from django.conf.urls import url
from django.urls import path

#This is accessing the views methods/functions we wrote
from .views import indexPageView, orderPageView
from .views import aboutPageView
from .views import productPageView

#Create the paths

urlpatterns = [
    path('',indexPageView, name="Home"),
    path('about/',aboutPageView, name="About"),
    path('products/',productPageView, name="Products"),
    path('orderpage/',orderPageView,name="OrderPage")
]

