from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)  # auto_now(자동 디비 업데이트)
    updated = models.DateTimeField(auto_now=True)
  
    # 이 모델을 db에 추가하지 않기위해 추상모델로 만듬
    class Meta:
        abstract = True