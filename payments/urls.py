from django.urls import path
from . import views
urlpatterns = [
    path('reservation/', views.PaymentproductList.as_view(), name="reservation"),
]
