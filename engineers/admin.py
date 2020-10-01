from django.contrib import admin
from .models import Engineer
# Register your models here.

@admin.register(Engineer)
class EngineerAdmin(admin.ModelAdmin):
    '''
    EngineerAdmin 설정하기
    '''
    fieldsets = (
        (
            'Information',
            {"fields": ("name","number","days", "times", "image")},
        ),
    )

    list_display = (
        'name',
        'number',
        'days',
        'times',
    )