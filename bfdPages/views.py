from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def indexPageView(request):
    return render(request, "bfdPages/index.html")


def aboutPageView(request):
    return HttpResponse("About Page")


def productPageView(request):
    return HttpResponse("Product list page")

def orderPageView(request) :
    return HttpResponse("Order page")