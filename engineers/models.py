from django.db import models
import datetime as dt

# 설치 기사 모델
# creater - minseok
class Engineer(models.Model):
    name = models.CharField(max_length=10) # 설치기사 이름
    number = models.CharField(max_length=20) # 연락처
    image = models.ImageField(upload_to="engineer_photos") # 설치기사 사진
    affiliation = models.CharField(max_length=20) # 설치기사 소속
    
    
    def __str__(self):
        return self.name
        
        # 기사 이름으로 admin에서 관리하도록함.


#[형민] 엔지니어 스케줄 model

class Schedule(models.Model) :

    scheduled_date = models.DateField()     # 예약된 날짜
    scheduled_time = models.TimeField(default=dt.time(00, 00))     # 예약된 시간
    engineer = models.ForeignKey("engineers.Engineer",related_name="schedule", on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.engineer.name