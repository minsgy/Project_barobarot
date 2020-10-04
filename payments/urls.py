from django.urls import path
from . import views
urlpatterns = [
    path('reservation/', views.ReservaionList.as_view(), name="reservation"),

]
