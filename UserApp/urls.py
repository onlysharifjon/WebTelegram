from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', Registratsiya.as_view(), name='Registratsiya qismi'),
    path('signin/', LoginApi.as_view(), name='Signin qismi'),
]
