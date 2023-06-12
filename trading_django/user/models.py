from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

# Create your models here.
class User(AbstractBaseUser):
    '''
        이메일
        이름
        비밀번호
    '''

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    class Meta:
        db_table = "User"
