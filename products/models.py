from django.db import models

#[형민] Product 모델

class Product(models.Model):

    ''' Product model '''

    product_name = models.CharField(max_length=50)
    sale = models.FloatField()                          #할인율
    price = models.IntegerField()
    manufacture = models.CharField(max_length=50)     #제조사
    rating = models.DecimalField(max_digits=2, decimal_places=1)        #10점 내 평점
    product_image = models.ImageField(upload_to="product/product_image")
    #상품 상세설명
    image_description = models.ImageField(upload_to="product/image_description")

    # 할인된 가격 
    def set_saleprice(self):
        if self.sale != None:
            return round(self.price*((100.0-self.sale)/100))    #반올림
        else :
            return print("fail")

    def __str__(self):
        return self.product_name 
