
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.

@api_view(["POST"])
def api_response(request):
    operation_type = request.POST.get('operation_type')
    print(operation_type)
    x = int(request.POST.get('x'))
    y = int(request.POST.get('y'))

    if operation_type == "addition":
        result = x + y
        
    elif operation_type == "multiplication":
        result = x * y
        
    elif operation_type == "subtraction":
        result = x - y
        
    
    else:
        operation_type = "Invalid Operator"
        result = 0

    return JsonResponse({'slackUsername':'Johanan Amoateng','result':result,'operation_type':operation_type})
        
    
