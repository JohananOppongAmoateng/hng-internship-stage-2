
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.

@api_view(["POST"])
def api_response(request):
    
    operation_type = request.POST['operation_type']
    x = int(request.POST['x'])
    y = int(request.POST['y'])
    result = 0

    if operation_type == "addition":
        result = x + y

    elif operation_type == "multiplication":
        result = x * y
    
    elif operation_type == "subtraction":
        result = x - y
        
    return Response({'slackUsername':'Johanan Amoateng','result':result,'operation_type':operation_type})
