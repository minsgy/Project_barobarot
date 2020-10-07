from django.db import models
from core import models as core_models
import random
# Create your models here.
# Creater - minseok 

# 주문 번호 랜덤 함수 8자
def random_string():
      return str(random.randint(00000000, 99999999)) 

class Paymentproduct(core_models.TimeStampedModel):
   product = models.ForeignKey('products.Product', related_name='payments',on_delete=models.CASCADE) # 연결 된 상품
   user = models.ForeignKey('users.User', related_name='payments', on_delete=models.CASCADE) # 주문한 사용자
   engineer = models.ForeignKey('engineers.Engineer',related_name='payments' ,on_delete=models.CASCADE) # 연결 된 설치기사
  
   amount = models.PositiveIntegerField(default=0) # 물건 수량 , product의 price와 사칙연산 예정(*)
   address = models.CharField(max_length=30) # 주소 검색 API 구현
   
   created_time = core_models.TimeStampedModel.created # 주문 시간 - 객체 생성 시간
   visit_date = models.DateTimeField() # 방문 날짜 및 시간

   # def create_time_string(self):
   #    return self.str(created_time) + random_string

   order_number = models.CharField(max_length=30, default=random_string) # 주문번호 - 생성날짜 + random_string 합쳐서 문자열 생성

   def __str__(self):
      return f"{self.user} - {self.engineer}"
          