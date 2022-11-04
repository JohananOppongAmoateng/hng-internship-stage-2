
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.

@api_view(["POST"])
def api_response(request):
    
    operation_type = request.POST['operation_type']
    x = int(request.POST['x'])
    y = int(request.POST['y'])

    if operation_type == "addition":
        result = x + y
        return Response({'slackUsername':'Johanan Amoateng','result':result,'operation_type':operation_type})

    elif operation_type == "multiplication":
        result = x * y
        return Response({'slackUsername':'Johanan Amoateng','result':result,'operation_type':operation_type})
    
    elif operation_type == "subtraction":
        result = x - y
        return Response({'slackUsername':'Johanan Amoateng','result':result,'operation_type':operation_type})
    
    else:
        operation_type = "Invalid Operator"
        result = 0
        return Response({'slackUsername':'Johanan Amoateng','result':result,'operation_type':operation_type})
        
    
