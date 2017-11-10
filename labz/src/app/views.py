from django.shortcuts import render
try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except:
    pass

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Profesor
from .forms import CreateForm
# Create your views here.


def list(request):
    #main page
    inf = Profesor.objects.all()

    context = {
        "prof_list": inf,


    }
    return render(request,"base.html",context)


def news_create(request):
    form = CreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        messages.success(request, "Post Created")
        return HttpResponseRedirect(post.id)
    context = {
        "form": form
    }
    return render(request, "post_form.html", context)

def personal_info(request):

    return render(request,"personal_info.html")
def create_prof(request):


    return render(request,"history.html")

def history(request):

    return render(request,"history.html")


