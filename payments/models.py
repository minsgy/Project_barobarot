from django.db import models
from core import models as core_models
import random
# Create your models here.
# Creater - minseok 

# 주문 번호 랜덤 함수 8자
def random_string():
      return str(random.randint(2020000000, 9999999999)) 

class Paymentproduct(core_models.TimeStampedModel):
      receiver = models.OneToOneField('Receiver', on_delete=models.CASCADE) # 연결 된 받는사람 정보 
      product = models.ForeignKey('products.Product', related_name='payments',on_delete=models.CASCADE) # 연결 된 상품
      user = models.ForeignKey('users.User', related_name='payments', on_delete=models.CASCADE) # 주문한 사용자
      engineer = models.ForeignKey('engineers.Engineer',related_name='payments' ,on_delete=models.CASCADE) # 연결 된 설치기사

      amount = models.PositiveIntegerField(default=0) # 물건 수량 , product의 price와 사칙연산 예정(*)
      address = models.CharField(max_length=30, null=True) # 주소 검색 API 구현

      created_time = core_models.TimeStampedModel.created # 주문 시간 - 객체 생성 시간
      visit_date = models.DateField() # 방문 날짜 및 시간
      visit_time = models.TimeField()     
   
      order_number = models.CharField(max_length=30, default=random_string) # 주문번호 - 생성날짜 + random_string 합쳐서 문자열 생성      
      
      def __str__(self):
         return f"{self.user} - {self.engineer}"
      def total_price(self):
            return int(self.amount * (self.product.price - (self.product.price * (self.product.sale / 100.0))))

class Receiver(models.Model):  
      ''' 주문 아이템 - 받는 사람 정보''' 
      receiver_name = models.CharField(max_length=10) # 받는 사람 이름
      receiver_number = models.CharField(max_length=15) # 받는 사람 연락처
      receiver_plus_number = models.CharField(max_length=15) # 받는 사람 추가 연락처
      zip_code = models.PositiveIntegerField(default=0) # 우편 번호
      address = models.CharField(max_length=30) # 주소
      delivery_message = models.CharField(max_length=50) # 배송 메세지

      def __str__(self):
            return self.receiver_name