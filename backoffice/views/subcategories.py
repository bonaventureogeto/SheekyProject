from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#List subcaegories
def index(request):
    if request.user.is_authenticated:
        return render(request,'backend/subcategories/index.html')
    else:
        return render(request,'backend/auth/login.html')

#Show create subcategory form
def create(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/app/subcategories/create')
    else:
        return render(request,'backend/auth/login.html')