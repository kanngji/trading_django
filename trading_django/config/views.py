from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
# 스크래핑

import requests
from bs4 import BeautifulSoup

from datetime import datetime

# Create your views here.
class Main(APIView):
    def get(self,request):
        # 로고 주소
        logo_url = "static/img/logo.PNG"
        crs1 = "static/img/finbiz.PNG"
        crs2 = "static/img/hangyoung.PNG"
        crs3 = "static/img/tradingview.PNG"
        time = datetime.now
        context = {'logo_url':logo_url,'crs1':crs1,'crs2':crs2,'crs3':crs3,'time':time}
        
        return render(request, 'index.html',context)
    
class GetData(APIView):
    def get(self,request):
        res = requests.get('https://www.paxnet.co.kr/stock/sise/industry?wlog_rpax=R_industry')
        soup = BeautifulSoup(res.content,'html.parser')
        
        # 코스피 상승업종 top3 스크래핑
        kospi_top3_stocks1 = soup.select_one('#contents > div.cont-area > div.h-table.swiper-container > div.thema-top3.swiper-wrapper > dl:nth-child(1) > dd > ul > li:nth-child(1)')
        kospi_top3_stocks2 = soup.select_one('#contents > div.cont-area > div.h-table.swiper-container > div.thema-top3.swiper-wrapper > dl:nth-child(1) > dd > ul > li:nth-child(2)')
        kospi_top3_stocks3 = soup.select_one('#contents > div.cont-area > div.h-table.swiper-container > div.thema-top3.swiper-wrapper > dl:nth-child(1) > dd > ul > li:nth-child(3)')
        
        # 코스닥 상승업종 top3 스크래핑
        kosdaq_top3_stocks1 = soup.select_one('#contents > div.cont-area > div.h-table.swiper-container > div.thema-top3.swiper-wrapper > dl:nth-child(2) > dd > ul > li:nth-child(1)')
        kosdaq_top3_stocks2 = soup.select_one('#contents > div.cont-area > div.h-table.swiper-container > div.thema-top3.swiper-wrapper > dl:nth-child(2) > dd > ul > li:nth-child(2)')
        kosdaq_top3_stocks3 = soup.select_one('#contents > div.cont-area > div.h-table.swiper-container > div.thema-top3.swiper-wrapper > dl:nth-child(2) > dd > ul > li:nth-child(3)')

        kospi_list1=[]
        kospi_list2=[]
        kospi_list3=[]
        kosdaq_list1=[]
        kosdaq_list2=[]
        kosdaq_list3=[]
        for i in kospi_top3_stocks1:
            if i.get_text()=='':
                continue
            else:
                kospi_list1.append(i.get_text().strip())
        
        for i in kospi_top3_stocks2:
            if i.get_text()=='':
                continue
            else:
                kospi_list2.append(i.get_text().strip())

        for i in kospi_top3_stocks3:
            if i.get_text()=='':
                continue
            else:
                kospi_list3.append(i.get_text().strip())



        for i in kosdaq_top3_stocks1:
            if i.get_text()=='':
                continue
            else:
                kosdaq_list1.append(i.get_text().strip())
        
        for i in kosdaq_top3_stocks2:
            if i.get_text()=='':
                continue
            else:
                kosdaq_list2.append(i.get_text().strip())

        for i in kosdaq_top3_stocks3:
            if i.get_text()=='':
                continue
            else:
                kosdaq_list3.append(i.get_text().strip())
           
        
        new_list1 = [item for item in kospi_list1 if item != '']
        kospi_list1 = [item.split('\n')[0] for item in new_list1]

        new_list2 = [item for item in kospi_list2 if item != '']
        kospi_list2 = [item.split('\n')[0] for item in new_list2]

        new_list3 = [item for item in kospi_list3 if item != '']
        kospi_list3 = [item.split('\n')[0] for item in new_list3]

        new_list4 = [item for item in kosdaq_list1 if item != '']
        kosdaq_list1 = [item.split('\n')[0] for item in new_list4]

        new_list5 = [item for item in kosdaq_list2 if item != '']
        kosdaq_list2 = [item.split('\n')[0] for item in new_list5]

        new_list6 = [item for item in kosdaq_list3 if item != '']
        kosdaq_list3 = [item.split('\n')[0] for item in new_list6]



        data = {
            'kospi_list1': kospi_list1,
            'kospi_list2': kospi_list2,
            'kospi_list3': kospi_list3,
            'kosdaq_list1': kosdaq_list1,
            'kosdaq_list2': kosdaq_list2,
            'kosdaq_list3': kosdaq_list3
        }
        return Response(data)
        # if news_title:
        #     print(news_title)
        #     return Response(status=200)
        # else:
        #     return Response("News title not found", status=404)


