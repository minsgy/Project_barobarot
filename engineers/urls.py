from django.urls import path
from . import views
urlpatterns = [
    path('engineer_list/', views.ListEngineer.as_view(), name="engineer"),
]
