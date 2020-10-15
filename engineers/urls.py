from django.urls import path
from . import views

app_name="engineers"

urlpatterns = [
    path('engineer_list/', views.ListEngineer.as_view(), name="engineer"), # 기사 리스트 url
    path('engineer_list/<int:pk>', views.DetailEngineer.as_view(), name="detail"), # 기사 개인 프로필 url
    path('engineer_list/<int:pk>/review', views.DetailReview.as_view(), name="read_review"), # 리뷰 읽기 전용

]
