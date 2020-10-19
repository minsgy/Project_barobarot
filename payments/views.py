from datetime import datetime
from django.db.models import query

from engineers.models import Engineer, Schedule
from django.http import request
from django.views.generic.base import TemplateView
import engineers
from payments.models import Paymentproduct, core_models, Receiver
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import models
from products import models as product_model
from users import models as user_model
from engineers import models as engineer_model
from core import models as core_model

from engineers.forms import MyForm  #엔지니어 폼(스케줄) - 시간단위 입력
# [형민] reservation view
 
# 결제 상품(예약상품) 리스트
class PaymentproductList(ListView) :

    ''' Checking Reservation cbv '''

    model = models.Paymentproduct
    context_object_name = 'payment_products'      #넘겨지는 변수 이름
    template_name = 'order/__order_list.html' # Default 연결 값 변경   

    
# 결제 상품의 상품 불러옴
class payment_do(DetailView):

    ''' payment doing cbv '''
    
    model = product_model.Product   
    context_object_name = 'products'      #넘겨지는 변수 이름
    template_name = 'payments/__payment.html' # Default 연결 값 변경 
    # 넘겨지는 변수 추가(복수개의 객체 전송)

    # total_price = self.object.price
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.kwargs['pk']를 통해서 url에서 pk값을 받을 수 있다.
        # url은 `path('<pk>/', PhotoView.as_view())으로 구현되어있어서 해당 pk 부분을 받아와야함
        context['amount'] = self.request.GET.get('amounts') # 전 페이지에서 수량 값 받아옴.
        context['paymentproducts'] = models.Paymentproduct
        context['engineers'] = engineer_model.Engineer.objects.all()        #모든 엔지니어 데이터 넘기기
        context['form'] = MyForm()       #시간단위 입력 폼
        
        
        return context  

        
# 결제 상품 생성
def PaymentproductCreate(request, product_pk, user_pk):

    ''' Create paymentproduct fbv ''' 

    if request.method == 'POST':
        # print('engineer-pk -----------', request.POST.get('engineer-pk'))
        # print('date -----------', request.POST.get('date'))
        # print('time -----------', request.POST.get('time'))
        paymentproducts = Paymentproduct() # 객체 클래스 적용
        products_data = product_model.Product.objects.get(pk=product_pk)
        user_data = user_model.User.objects.get(pk=user_pk)
        engineer_data = engineer_model.Engineer.objects.get(pk=(request.POST.get('engineer-pk')))   #엔지니어 연결

        print('address---------',request.POST.get('ship-message'))
    
        split_address = request.POST.get('address')
        addresss_zip_code = int(float(split_address[1:6]))  # 주소창에서 우편번호 뽑기 , int 형 변환을 위해서 먼저 float로 해야함.
        address_name = split_address[7:] # 주소창에서 주소 이름 뽑기

        # form = MyForm(request.POST, request.FILES)      #form 파일로 데이터 받아오기

        # --------------------------------------------------------------------------
        receiver_data = Receiver()
        receiver_data.receiver_name = request.POST.get('receiver_name')
        receiver_data.receiver_number = request.POST.get('receiver_number')
        receiver_data.receiver_plus_number = request.POST.get('receiver_number2')
        receiver_data.zip_code = addresss_zip_code
        receiver_data.address = address_name
        receiver_data.delivery_message = request.POST.get('ship-message')

        receiver_data.save()

        # --------------------------------------------------------------------------------------
        print("엔지니어 pk : ",request.POST.get('engineer-pk'))
        paymentproducts.product = products_data
        paymentproducts.user = user_data
        paymentproducts.engineer = engineer_data
        paymentproducts.receiver = receiver_data

        paymentproducts.amount = request.POST.get('amount') # 수량값 저장되게
        paymentproducts.address = address_name

        # paymentproducts.created_time = core_models.TimeStampedModel.created
        paymentproducts.visit_date = request.POST.get('date')
        paymentproducts.visit_time = request.POST.get('time')    #form fields 값 가져오기

        # -------------------------------------------------------------------------------------

        # amount 값과 물건 가격의 값을 곱해 합 가격을 구합니다.
        # paymentproducts.total_price = paymentproducts.amount * paymentproducts.product.price 
            
        schedule = Schedule()
        schedule.engineer = engineer_data
        schedule.scheduled_date = request.POST.get('date')
        schedule.scheduled_time = request.POST.get('time')
            
        schedule.save()

        paymentproducts.save()

        return redirect('payments:order_success', user_pk, paymentproducts.pk )
            # 생성 된 주문 아이템 pk, 로그인한 user_pk 가지고 가기

    return render(request, 'payments/__payment.html')


''' 주문 성공 함수 '''
def order_success(request, user_pk, payment_pk):
    
    payment = Paymentproduct.objects.get(pk=payment_pk)
    user = user_model.User.objects.get(pk=user_pk)
    
    def getPoint():
        return int(payment.product.price * 0.025)

    context = {
        'payment':payment,
        'user':user, 
        'getPoint':getPoint(),   
    }


    return render(request, 'payments/__order_success.html', context)
    

''' 주문 detail 함수 '''

def order_detail(request, pk):
    payment = Paymentproduct.objects.get(pk=pk)
    return render(request, 'order/__order_detail.html', {'payments':payment})



''' 주소 popup '''

def popup(request) :
    return render(request, 'payments/__payment_address_popup.html')

def payment_engineer_popup(request) :
    return render(request, 'payments/__payment_engineer_info.html')

def engineer_json_test(request):
    if (request.method == 'POST'):
        import json
        json_dic = json.loads(request.body)
        # PK
        from engineers import models as engineer_model
        engineers = engineer_model.Engineer.objects.all()
        json_dic['engineers'] = engineers;
        
        view_dic = [] 
        count =0

        for one in engineers:           
            for a in one.schedule.all() :      
                if str(a.scheduled_date) == json_dic['date'] and str(a.scheduled_time) == json_dic['time'] :
                    count+=1
            
            if(count==0):
                print(one)
                view_dic.append(one)
            
            count=0
            
        print("뷰딕",view_dic), 
        json_dic['variable_angs'] = view_dic
        print("재딕",json_dic)
        # json_dic 에 담기는 정보:dict => date(날짜):str, time(시간):str, variable : 가능한 엔지니어 정보
        return render(request, 'engineers/engineers_list.html', json_dic)
