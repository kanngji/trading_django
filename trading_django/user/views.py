
from django.shortcuts import render
from rest_framework.views import APIView
from requests import Response
from django.http import HttpResponse, JsonResponse

from .models import User
# Create your views here.

class Main(APIView):
    def get(self,request):
        return HttpResponse("야야야")
    
class Login(APIView):
    def get(self,request):
        return render(request, 'user/login.html')
    
    def post(self,request):
        email = request.data.get('email',None)
        password = request.data.get('password',None)

        user = User.objects.filter(email=email).first()

        if user is None:
            return JsonResponse({"message":"잘못된 회원정보입니다."})

        if user.password == password:
            request.session['email'] = email
            return HttpResponse(status=200)
        else:
            return JsonResponse({"message":"잘못된 회원정보입니다."})
          
class Register(APIView):
    def get(self,request):    
        return render(request,'user/register.html')
    
    def post(self,request):
        email = request.data.get('email',None)
        name = request.data.get('name',None)
        password1 = request.data.get('password1',None)
        password2 = request.data.get('password2',None)

        if password1 != password2 :
            return JsonResponse({"password_error_message":"비밀번호를 일치하게 입력해주세요"})
        
        User.objects.create(email=email,
                            name=name,
                            password=password1)
        # 회원가입 성공
        return HttpResponse(status=200)


class checkEmailDuplicateView(APIView):
    def post(self,request):
        email = request.data.get('email',None)

        # 이메일이 가입되어 있따면
        if User.objects.filter(email=email).exists():
            
            return JsonResponse({'email_exists':True},status=201)
        # 이메일이 없다면
        else:
            return JsonResponse({'email_exists':False},status=201)


