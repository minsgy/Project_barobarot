from django.shortcuts import render, redirect
from .models import Comment
from engineers.models import Engineer
from django.core.exceptions import PermissionDenied
# Create your views here.

def createComment(request, eg_pk):

    engineer = Engineer.objects.get(pk=eg_pk)
    if request.method == 'POST':
        comment = Comment()
        comment.engineer = engineer
        comment.user = request.user
        comment.content = request.POST.get('reviewText')
        comment.save()
        return redirect('engineers:detail', eg_pk) 

def deleteComment(request, eg_pk, cm_pk):

    comment = Comment.objects.get(pk=cm_pk)
    if request.user == comment.user:
        comment.delete()
        return redirect('engineers:detail', eg_pk)
    else:
        raise PermissionDenied
