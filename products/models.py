from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import random
import string
#[형민] Product 모델
#[minseok] 10. 11 - 필드 추가 (모델코드)

# random 모델코드 생성 함수
def model_code():
    string_pool = string.ascii_uppercase + string.digits # 대문자 + 숫자
    result = ""
    for i in range(10):
        result += random.choice(string_pool)
    return result


class Product(models.Model):

    ''' Product model '''
    product_name = models.CharField(max_length=50) #물건 이름
    sale = models.FloatField() #할인율
    price = models.PositiveIntegerField(default=0, blank=True)
    manufacture = models.CharField(max_length=50)     #제조사
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])  #최소/최대 평점 0.0 ~ 5.0
    product_image = models.ImageField(upload_to="product/product_image")
    #상품 상세설명
    image_description = models.ImageField(upload_to="product/image_description")

    #모델 코드  
    model_code = models.CharField(max_length=12, default=model_code) # 대문자+숫자


    # 할인된 가격 
    def set_saleprice(self):
        if self.sale != None:
            return round(self.price*((100.0-self.sale)/100))    #반올림
        else :
            return print("fail")

    def __str__(self):
        return self.product_name 
