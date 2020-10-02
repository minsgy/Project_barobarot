from django.db import models

#[형민] Product 모델

class Product(models.Model):

    ''' Product model '''

    product_name = models.CharField(max_length=50)
    sale = models.FloatField()                          #할인율
    price = models.IntegerField()
    manufacture = models.CharField(max_length=50)     #제조사
    product_image = models.ImageField(upload_to="product/product_image")
    #상품 상세설명
    image_description = models.ImageField(upload_to="product/image_description")

    def __str__(self):
        return self.product_name