from django.db import models
from core import models as core_models
# Create your models here.
# Creater - minseok 

class Paymentproduct(core_models.TimeStampedModel):
   product = models.ForeignKey('products.Product', related_name='payments',on_delete=models.CASCADE) # 연결 된 상품
   user = models.ForeignKey('users.User', related_name='payments', on_delete=models.CASCADE) # 주문한 사용자
   engineer = models.ForeignKey('engineers.Engineer',related_name='payments' ,on_delete=models.CASCADE) # 연결 된 설치기사
  
   amount = models.IntegerField() # 물건 수량 , product의 price와 사칙연산 예정(*)
   address = models.CharField(max_length=30) # 주소 검색 API 구현
   
   created_time = core_models.TimeStampedModel.created # 주문 시간 - 객체 생성 시간
   visit_date = models.DateTimeField() # 방문 날짜 및 시간

   def __str__(self):
      return f"{self.user} - {self.engineer}"
          