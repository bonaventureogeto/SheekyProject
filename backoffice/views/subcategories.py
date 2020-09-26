from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages

from ..models.subcategories import Subcategory

#List subcaegories
def index(request):
    if request.user.is_authenticated:
        subcategories_list=Subcategory.objects.all

        context = {
            'subcategories_list': subcategories_list,
        }

        return render(request,'backend/subcategories/index.html',context)
    else:
        return render(request,'backend/auth/login.html')

#Show create subcategory form
def create(request):
    if request.user.is_authenticated:
        return render(request,'backend/subcategories/create.html')
    else:
        return render(request,'backend/auth/login.html')

#Store subcategory
def store(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            subcategory_name = request.POST.get('subcategory_name', '')
            date_created = timezone.now()
            date_updated = timezone.now()

            s=Subcategory()
            s.sub_category_name=subcategory_name
            s.created_at=date_created
            s.updated_at=date_updated
            s.save()

            messages.success(request, 'Record saved successfully!')
            return HttpResponseRedirect('/app/subcategories/index')

        else:
            messages.error(request, 'Please subcategory name to proceed!')
            return render(request,'backend/subcategories/create.html')
    else:
        return HttpResponseRedirect('/app/login')