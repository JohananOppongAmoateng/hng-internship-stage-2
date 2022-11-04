
from .views import api_response
from django.urls import path

urlpatterns = [
    path("",api_response,name="jsonresponse")    
    ]