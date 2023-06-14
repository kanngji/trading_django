from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import Main,Register


urlpatterns = [
    path('',Main.as_view()), # 일단 확인
    path('register/',Register.as_view()) #로그인확인
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)