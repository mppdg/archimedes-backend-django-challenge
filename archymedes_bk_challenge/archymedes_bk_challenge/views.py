from django.shortcuts import redirect
from rest_framework.response import Response

def redirect_api_view(request):
    response = redirect('/api/v1/users')
    return response