
from django.shortcuts import render
from rest_framework.views import APIView
from requests import Response
from django.http import HttpResponse
# Create your views here.

class Main(APIView):
    def get(self,request):
        return HttpResponse("야야야")
    
class Register(APIView):
    def get(self,request):
        
        
        return render(request,'user/register.html')
