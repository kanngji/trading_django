from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class Main(APIView):
    def get(self,request):
        return render(request, 'index.html')