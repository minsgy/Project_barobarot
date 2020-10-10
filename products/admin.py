from django.contrib import admin
from . import models

# [ 형민 ] product admin custom

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    ''' Product admin Custom '''

    list_display = (
        "product_name",
        "sale",
        "price",
        "set_saleprice",
        "manufacture",
        "product_image",
        "rating",
    ) 