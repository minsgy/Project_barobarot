from django.db import models
from django.contrib.auth.models import AbstractUser

#[형민] User 모델

class User(AbstractUser):

    ''' User Model '''

    name = models.CharField(max_length=50, unique=True )
    number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    # superhost = models.BooleanField(default=False)

    def __str__(self):
        return self.name