from django.urls import path
from . import views

# app_name = comments
urlpatterns = [
    path('<int:cm_pk>/<int:user_pk>', views.createComment, name='create_comment'),
]
