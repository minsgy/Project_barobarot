from django.db import models
from core import models as core_models
# Create your models here.
# Creater - minseok 

class Paymentproduct(core_models.TimeStampedModel):

   ''' 사용자 배달 주문 아이템 '''

   product = models.ForeignKey('products.Product', related_name='payments',on_delete=models.CASCADE) # 연결 된 상품
   user = models.ForeignKey('users.User', related_name='payments', on_delete=models.CASCADE) # 주문한 사용자
   engineer = models.ForeignKey('engineers.Engineer',related_name='payments' ,on_delete=models.CASCADE) # 연결 된 설치기사
  
   amount = models.IntegerField() # 물건 수량 , product의 price와 사칙연산 예정(*)
   address = models.CharField(max_length=30) # 주소 검색 API 구현
   
   created_time = core_models.TimeStampedModel.created # 주문 시간 - 객체 생성 시간
   visit_date = models.DateTimeField() # 방문 날짜 및 시간

   def __str__(self):
      return f"{self.user} - {self.engineer}"
          

class Receiver(models.Model):

   ''' 주문 아이템 - 받는 사람 정보'''

   paymentproduct = models.OneToOneField('Paymentproduct', on_delete=models.CASCADE) 
   # 주문 아이템과 1:1 관계, 주문 아이템과 연결 된 배달 정보

   receiver = models.CharField(max_length=10) # 받는 사람 이름
   receiver_number = models.CharField(max_length=15) # 받는 사람 연락처
   receiver_plus_number = models.CharField(max_length=15) # 받는 사람 추가 연락처
   zip_code = models.PositiveIntegerField(default=0) # 우편 번호
   address = models.CharField(max_length=30) # 주소
   delivery_message = models.CharField(max_length=50) # 배송 메세지

   