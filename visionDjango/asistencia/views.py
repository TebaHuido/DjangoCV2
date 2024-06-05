from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.middleware.csrf import get_token

# Create your views here.
def vision(req):
    csrf_token = get_token(req)
    print(csrf_token)
    return HttpResponse("hello")

class TestView(View):
    def post(self, request, *args, **kwargs):
        print(request.POST.get('person', 'No person'))
        return HttpResponse("100")
    def get(self, request, *args, **kwargs):
        return HttpResponse("100")