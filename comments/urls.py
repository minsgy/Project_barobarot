from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('<int:eg_pk>', views.createComment, name='create_comment'),
    path('delete/<int:eg_pk>/<int:cm_pk>', views.deleteComment, name='delete_comment'),
]
