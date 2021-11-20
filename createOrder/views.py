from django.shortcuts import render

# Create your views here.


def orderPageView(request):
    return render(request, 'createOrder/createOrder.html')
