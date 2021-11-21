from django.shortcuts import render
# this view function needs to send the RESPONSE
from django.http import HttpResponse

# redirect
from django.shortcuts import redirect

# Create your views here.


def orderPageView(request):
    return render(request, 'createOrder/createOrder.html')


# these are for the sessions, which were not working ################3
def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>dataflair</h1>")


def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("dataflair<br> cookie createed")
    else:
        response = HttpResponse(
            "Dataflair <br> Your browser doesnot accept cookies")
    return response


def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>dataflair<br> the session is set</h1>")


def access_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(
            request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create/')
