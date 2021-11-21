# THIS IS THE URL's that is for our specific app
from django.urls import path

# This is accessing the views/funcitons that we wrote on views.py!!
from .views import cookie_session
from .views import cookie_delete
from .views import create_session
from .views import access_session


# we create the path with this syntax
urlpatterns = [

    path('testcookie/', cookie_session, name='cookie'),
    path('deletecookie/', cookie_delete, name='cookieDelete'),
    path('create/', create_session),
    path('access', access_session)
]
