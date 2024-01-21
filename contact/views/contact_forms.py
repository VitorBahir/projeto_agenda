from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render 
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator


def create(request):
    
    context = {
        
    }
    return render(
        request,
        'contact/create.html',
        context
    )
