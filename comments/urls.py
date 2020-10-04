from django.urls import path
from . import views

# app_name = comments
urlpatterns = [
    path('', views.createComment, name='create_comment'),
]
