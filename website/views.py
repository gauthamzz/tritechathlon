from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from .models import Ranking
from django.db.models import Q
import datetime
# Create your views here.
def rank(request):
    queryset_list=Ranking.objects.all().order_by("-score")
    query = request.GET.get("q")
    if query:
    	queryset_list=queryset_list.filter(Q(username__icontains=query)).distinct()
    paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
    	    # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
    	    # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context={
    "object_list":queryset
    }
    return render(request,"ranking.html",context)

def home(request):
    if request.user.is_authenticated():
        who=0
    else:
        who=1
    whoami=request.user.username
    context={
    "who":who,
    "whoami":whoami
    }
    return render(request,"index.html",context)

def rules(request):
    if request.user.is_authenticated():
        who=0
    else:
        who=1
    whoami=request.user.username
    context={
    "who":who,
    "whoami":whoami
    }
    return render(request,"rules.html",context)

def contact(request):
    if request.user.is_authenticated():
        who=0
    else:
        who=1
    whoami=request.user.username
    context={
    "who":who,
    "whoami":whoami
    }
    return render(request,"contact.html",context)

def contact(request):
    if request.user.is_authenticated():
        who=0
    else:
        who=1
    whoami=request.user.username
    context={
    "who":who,
    "whoami":whoami
    }
    return render(request,"contact.html",context)
