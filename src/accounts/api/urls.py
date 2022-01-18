from django.urls import path, include

app_name = 'user-api'

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', obtain_auth_token, name="login"),
]