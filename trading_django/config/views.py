from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class Main(APIView):
    def get(self,request):
        # 로고 주소
        logo_url = "static/img/logo.PNG"
        return render(request, 'index.html',{'logo_url':logo_url})