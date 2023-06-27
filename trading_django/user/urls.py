from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import Main,Login,Register,checkEmailDuplicateView


urlpatterns = [
    path('',Main.as_view()), # 일단 확인
    path('register/',Register.as_view()), # 회원가입화면
    path('login/',Login.as_view()), # 로그인 화면
    path('check_email_duplicate/',checkEmailDuplicateView.as_view()) #이메일 중복
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)