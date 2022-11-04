
from .views import api_response
from django.urls import path

urlpatterns = [
    path("sendjson",api_response,name="jsonresponse")    
    ]