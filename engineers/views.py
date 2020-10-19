from engineers.models import Engineer
from django.shortcuts import render, redirect
from . import models
from django.views.generic import ListView, DetailView
# Create your views here.

class ListEngineer(ListView): # ListView를 이용한 기사 나열

    model = models.Engineer
    context_object_name = 'engineers' # 객체를 부르는 이름
    template_name = 'engineers/engineers_list.html' # Default 연결 값 변경

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        context['count'] = int(0)
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     time = self.request.POST['time']
    #     print('ajfeoiwfjoefwjfojeifj', time)
    #     return context
    
class DetailEngineer(DetailView): # DetailView 리스트 값을 전부 반환함.

    model = models.Engineer
    context_object_name = 'engineers' # 객체를 부르는 이름
    template_name = 'engineers/__reviews.html' # Default 연결 값 변경    

class DetailReview(DetailView):
    model = models.Engineer
    context_object_name = 'engineers' # 객체를 부르는 이름
    template_name = 'engineers/__reviews_only_read.html' # Default 연결 값 변경    

    