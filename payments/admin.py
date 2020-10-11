from django.contrib import admin

# Register your models here.
from .models import Paymentproduct, Receiver
# Register your models here.

@admin.register(Paymentproduct)
class PaymentproductAdmin(admin.ModelAdmin):
    '''
    주문 한 물품 설정하기
    '''
    fieldsets = (
        (
            'Information',
            {"fields": ("receiver","product","user","engineer","amount","address" , "visit_date","visit_time",)},
        ),
    )

    list_display = (
        'receiver',
        'product',
        'user',
        'engineer',
        'amount',
        'address',
        'created_time',
        'visit_date',
        'visit_time',
        'order_number',
        'total_price',
    )

@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
    '''
    주문 한 물품, 받는 사람 설정하기
    '''
    fieldsets = (
        (
            'Information',
            {"fields": ("receiver_name","receiver_number","receiver_plus_number","zip_code","address" , "delivery_message")},
        ),
    )

    list_display = (
        'receiver_name',
        'receiver_number',
        'receiver_plus_number',
        'zip_code',
        'address',
        'delivery_message',
    )    