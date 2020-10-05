from django.shortcuts import render, redirect
from .models import Comment
from engineers.models import Engineer
from users.models import User
from django.urls import reverse
# Create your views here.

def createComment(request, cm_pk):

    engineer = Engineer.objects.get(pk=cm_pk)
   # user = User.objects.get(pk=user_pk)
    if request.method == 'POST':
        comment = Comment()
        comment.engineer = engineer
        comment.user = request.user
        comment.title = request.POST.get('title')
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('engineers:detail', cm_pk)


