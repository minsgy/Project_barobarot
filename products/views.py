from django.http import request
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator # paginator 적용
from products.models import Product
from engineers.models import Engineer
# from payments.models import Payments?
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from . import models
import random

# [형민] homeview
# minseok : 10. 18. paginator 추가
class HomeView(ListView):

    ''' home view cbv '''

    model = Product
    paginate_by = 10                    #한 페이지에 10 개 
    context_object_name = 'products'      #넘겨지는 변수 이름
    template_name = 'products/__home.html' # Default 연결 값 변경
    
def Searching_HomeView(request) :

    ''' Product Searching fbv '''

    Products = Product.objects.all()
    if request.GET.get:
        search = request.GET.get('search')
        print("검색어 확인",search, type(search))
        
        Products = Product.objects.all().filter(product_name__icontains = search)
        print("필터링",Products)
        return render(request, 'products/__search_home.html',{"products" : Products})
    
    return render(request, 'products/__home.html',{"products" : Products})


# [형민] product detail view
class ProductDetail(DetailView):

    ''' product detail view cbv'''

    model = Product  # Detailview를 사용하면 자동적으로 pk를 찾음
    context_object_name = 'products'                #넘겨지는 변수 이름
    template_name = 'products/__product_detail.html' # 전달 연결 값 변경

        

# Create DB File
def create_products(request):
    image_count = 0
    file = open('testfile/product_test.txt', mode='rt', encoding='UTF-8')
    file_list = file.readlines() # 라인단위로 읽어서 list 형식으로 저장
    for lists in file_list:
        image_count += 1
        temp = lists.split(',')
        product = Product(
            product_name = temp[1],
            sale = float(round(random.uniform(10, 30))),
            price = temp[2],
            manufacture = temp[0],
            rating = float(round(random.uniform(1, 5),1)), # 1.0~5.0 사이 실수 소수 첫째자리
            product_image = f"product/product_image/image{(image_count)}.jpg",
            image_description = f"product/product_image/image{(image_count)}.jpg",
        )
        # print(product.__dict__)
        product.save()
    file.close()

    # Engineer db 추가
    file2 = open('testfile/engineer_test.txt', mode='rt', encoding='UTF-8')
    file2_list = file2.readlines()
    image_count = 0 # 이미지 번호 초기화

    for lists2 in file2_list: 
        image_count += 1
        temp = lists2.split(',') 
        engineer = Engineer(
            name = temp[0],
            number = temp[1],
            affiliation = temp[2],
            image =  f"engineer_photos/engineer{(image_count)}.jpg",
        )
        engineer.save()
    file2.close()
    return redirect('products:home')
# def getHome(request):
#     return render(request, 'products/home.html')