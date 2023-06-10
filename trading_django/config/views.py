from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class Main(APIView):
    def get(self,request):
        # 로고 주소
        logo_url = "static/img/logo.PNG"
        crs1 = "static/img/finbiz.PNG"
        crs2 = "static/img/hangyoung.PNG"
        crs3 = "static/img/tradingview.PNG"
        context = {'logo_url':logo_url,'crs1':crs1,'crs2':crs2,'crs3':crs3}
        return render(request, 'index.html',context)