from django.shortcuts import render, redirect
from . import models
from django.views.generic import ListView
# Create your views here.

class ListEngineer(ListView): # ListView를 이용한 기사 나열

    model = models.Engineer
    context_object_name = 'engineers' # 객체를 부르는 이름
    template_name = 'engineers/engineers_list.html' # Default 연결 값 변경