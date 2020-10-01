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
            {"fields": ("engineer","amount","address" , "visit_date")},
        ),
    )

    list_display = (
        'engineer',
        'amount',
        'address',
        'created_time',
        'visit_date',
    )