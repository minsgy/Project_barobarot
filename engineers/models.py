from django.db import models
# 설치 기사 모델
# creater - minseok
class Engineer(models.Model):
    name = models.CharField(max_length=10) # 설치기사 이름
    number = models.CharField(max_length=20) # 연락처
    days = models.DateField() # yyyy-mm-dd 
    times = models.TimeField() # 시, 분, 초
    image = models.ImageField(upload_to="engineer_photos") # 설치기사 사진
    affiliation = models.CharField(max_length=20) # 설치기사 소속

    def __str__(self):
        return self.name
        
        # 기사 이름으로 admin에서 관리하도록함.