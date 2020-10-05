from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
# [ 형민 ] User admin custom

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    ''' User admin Custom '''

    fieldsets =  (
        (None, {"fields" : ("username","password","name", "number", "email")},),
    )
    
    list_display = (
        "username",
        "name",
        "email",
        "number",
    )

    # list_filter = UserAdmin.list_filter