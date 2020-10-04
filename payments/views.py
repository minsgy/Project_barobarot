from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from . import models

# [형민] reservation view

class ReservaionList(ListView) :

    ''' Checking Reservation cbv '''

    model = models.Paymentproduct
    context_object_name = 'reservations'      #넘겨지는 변수 이름
    template_name = 'reservation/check_reservaiton.html' # Default 연결 값 변경   

