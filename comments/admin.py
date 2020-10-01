from django.contrib import admin
from .models import Comment
# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''
    댓글 설정하기
    '''
    fieldsets = (
        (
            'Information',
            {"fields": ("title","content","engineer")},
        ),
    )

    list_display = (
        'title',
        'content',
        'engineer',
    )