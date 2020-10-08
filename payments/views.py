from django.http import request
from django.views.generic.base import TemplateView
import engineers
from payments.models import Paymentproduct, core_models
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import models
from products import models as product_model
from users import models as user_model
from engineers import models as engineer_model
from core import models as core_model


# [형민] reservation view
 
# 결제 상품(예약상품) 리스트
class PaymentproductList(ListView) :

    ''' Checking Reservation cbv '''

    model = models.Paymentproduct
    context_object_name = 'payment_products'      #넘겨지는 변수 이름
    template_name = 'reservation/check_reservation.html' # Default 연결 값 변경   

    
# 결제 상품의 상품 불러옴
class payment_do(DetailView):

    ''' payment doing cbv '''

    model = product_model.Product   
    context_object_name = 'products'      #넘겨지는 변수 이름
    
    template_name = 'payments/payment_doing.html' # Default 연결 값 변경 
    
    # 넘겨지는 변수 추가(복수개의 객체 전송)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.kwargs['pk']를 통해서 url에서 pk값을 받을 수 있다.
        # url은 `path('<pk>/', PhotoView.as_view())으로 구현되어있어서 해당 pk 부분을 받아와야함

        context['paymentproducts'] = models.Paymentproduct
        context['engineers'] = engineer_model.Engineer.objects.all()        #모든 엔지니어 데이터 넘기기
        return context

        
# 결제 상품 생성
def PaymentproductCreate(request, product_pk, user_pk):

    ''' Create paymentproduct fbv '''

    products_data = product_model.Product.objects.get(pk=product_pk)
    user_data = user_model.User.objects.get(pk=user_pk)
    engineer_data = engineer_model.Engineer.objects.get(pk=(request.POST.get('engineer')))   #엔지니어 연결

    print("엔지니어 pk : ",request.POST.get('engineer'))

    paymentproducts = get_object_or_404(Paymentproduct)

    if request.method == 'POST':

        paymentproducts.product = products_data
        paymentproducts.user = user_data
        paymentproducts.engineer = engineer_data

        paymentproducts.amount = request.POST.get('amount')
        paymentproducts.address = request.POST.get('adress')

        # paymentproducts.created_time = core_models.TimeStampedModel.created
        paymentproducts.visit_date = request.POST.get('visit')
 
        paymentproducts.save()
        return redirect('home')

    return render(request, 'payments/payment_doing.html', {'paymentproducts' : paymentproducts})