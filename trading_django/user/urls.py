from django.urls import path
from .views import Main

urlpatterns = [
    path('',Main.as_view()), # 일단 확인
]