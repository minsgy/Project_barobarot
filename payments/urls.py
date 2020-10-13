from os import name
from django.urls import path
from . import views


app_name='payments'

urlpatterns = [
    path('order_detail/<int:pk>', views.order_detail, name="order_detail"), # 주문 내역 상세 페이지
    path('order_list/', views.PaymentproductList.as_view(), name="order_list"), # 주문 내역 리스트 페이지
    path('paymentproduct/create/<int:product_pk>/<int:user_pk>/', views.PaymentproductCreate, name="paymentproduct_create"), # 주문 아이템 생성
    path('paymentproduct/<int:pk>/',views.payment_do.as_view(), name = "payment_do"), # 주문 페이지 입장
    path('order_success/<int:user_pk>/<int:payment_pk>/', views.order_success, name="order_success"), # 주문 성공 페이지 입장
    path('__payment_address_popup', views.popup, name="popup"),
    path('__payment_engineer_info', views.payment_engineer_popup, name="payment_engineer_popup"),
    path('engineer_json_test', views.engineer_json_test, name="json_test"),
]
