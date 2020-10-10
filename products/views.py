from django.views.generic.detail import DetailView
from products.models import Product
from django.shortcuts import render
from django.views.generic.list import ListView
from . import models

# [형민] homeview
class HomeView(ListView):

    ''' home view cbv '''

    model = models.Product
    paginate_by = 20                    #한 페이지에 20 개 
    paginate_orphans = 5                #한 페이지 5개이하는 전 페이지로

    context_object_name = 'products'      #넘겨지는 변수 이름
    template_name = 'products/__home.html' # Default 연결 값 변경

# [형민] product detail view
class ProductDetail(DetailView):

    ''' product detail view cbv'''

    model = models.Product  # Detailview를 사용하면 자동적으로 pk를 찾음
    context_object_name = 'products'                #넘겨지는 변수 이름
    template_name = 'products/product_detail.html' # Default 연결 값 변경




# def getHome(request):
#     return render(request, 'products/home.html')