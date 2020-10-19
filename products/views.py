from django.views.generic.detail import DetailView
from django.core.paginator import Paginator # paginator 적용
from products.models import Product
# from payments.models import Payments?
from django.shortcuts import render
from django.views.generic.list import ListView
from . import models

# [형민] homeview
# minseok : 10. 18. paginator 추가
class HomeView(ListView):

    ''' home view cbv '''

    model = models.Product
    paginate_by = 10                    #한 페이지에 10 개 
    context_object_name = 'products'      #넘겨지는 변수 이름
    template_name = 'products/__home.html' # Default 연결 값 변경



# [형민] product detail view
class ProductDetail(DetailView):

    ''' product detail view cbv'''

    model = models.Product  # Detailview를 사용하면 자동적으로 pk를 찾음
    context_object_name = 'products'                #넘겨지는 변수 이름
    template_name = 'products/__product_detail.html' # 전달 연결 값 변경

        

# Create DB File
def create_products(request):
    file = open('testfile/product_test.txt', mode='rt', encoding='UTF-8')
    file_list = file.readlines()
    for lists in file_list:
        temp = lists.split(',')
        # product = Product(
        #     product_name = temp[0],
        #     sale = temp[1],
        #     price = temp[2],
        #     manufacture = temp[3],
        #     rating = temp[4],
        #     product_image = temp[5]
        # )
        # products.save()

# def getHome(request):
#     return render(request, 'products/home.html')