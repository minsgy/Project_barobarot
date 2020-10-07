from django.contrib import admin

# Register your models here.
from .models import Paymentproduct
# Register your models here.

@admin.register(Paymentproduct)
class PaymentproductAdmin(admin.ModelAdmin):
    '''
    주문 한 물품 설정하기
    '''
    fieldsets = (
        (
            'Information',
            {"fields": ("product","user","engineer","amount","address" , "visit_date")},
        ),
    )

    list_display = (
        'product',
        'user',
        'engineer',
        'amount',
        'address',
        'created_time',
        'visit_date',
        'order_number',
    )