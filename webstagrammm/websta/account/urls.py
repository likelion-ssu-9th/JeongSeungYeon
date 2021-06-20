from django.urls import path
from .views import *

urlpatterns = [
    path('ssu_login/',login_view, name = "login"),
    path('logout/',logout_view, name = "logout"),
    path('signUp/',signup_view,name="signup"), 
]