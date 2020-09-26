from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages

from ..models.categories import Category
from ..models.subcategories import Subcategory
from ..forms.CategoryForm import CategoryForm

#List subcaegories
def index(request):
    if request.user.is_authenticated:
        categories=Category.objects.all

        context = {
            'categories': categories,
        }

        return render(request,'backend/categories/index.html',context)
    else:
        return render(request,'backend/auth/login.html')

#Show create subcategory form
def create(request):
    if request.user.is_authenticated:

        form=CategoryForm()

        subcategories=Subcategory.objects.all

        context = {
            'subcategories': subcategories,
            'form': form,
        }

        return render(request,'backend/categories/create.html',context)
    else:
        return render(request,'backend/auth/login.html')

#Store subcategory
def store(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            form = CategoryForm(request.POST)

            if form.is_valid():
                c = form.save(commit=False)
                c.created_at=timezone.now()
                c.updated_at=timezone.now()
                c.save()        

                messages.success(request, 'Record saved successfully!')
                return HttpResponseRedirect('/app/categories/index')
            else:
                return render(request,'backend/categories/create.html',{'form': form})
        else:
            return render(request,'backend/categories/create.html',{'form': form})
    else:
        return HttpResponseRedirect('/app/login')