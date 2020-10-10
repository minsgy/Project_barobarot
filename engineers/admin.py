from django.contrib import admin
from .models import Engineer, Schedule
# Register your models here.

@admin.register(Engineer)
class EngineerAdmin(admin.ModelAdmin):
    '''
    EngineerAdmin 설정하기
    '''
    fieldsets = (
        (
            'Information',
            {"fields": ("name","number", "image","affiliation")},
        ),
    )

    list_display = (
        'name',
        'number',
        "affiliation",
        # 'days',
        # 'times',
    )

    

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin) :

    model = Schedule

    list_display = ['get_engineer_name', 'scheduled_date', 'scheduled_time', ]
    
    def get_engineer_name(self, obj):
        return obj.engineer.name
    get_engineer_name.short_description = 'engineer Name'
    

     
