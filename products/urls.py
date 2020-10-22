from django.urls import path
from . import views

app_name='products'

urlpatterns = [
    # path('', views.getHome, name="home"),
    path('', views.HomeView.as_view(), name="home"),
    path('products/<int:pk>', views.ProductDetail.as_view(), name="product_detail"), # 상품상세url
    path('products_test/', views.create_products, name="products_create"),
    # path('products/amount/<int:pk>', views.products_amount_get, name="product_amount"), # 상품상세url
    path('product/search',views.Searching_HomeView, name="search"),
]
