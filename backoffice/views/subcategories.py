from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages

from ..forms.SubcategoryForm import SubcategoryForm
from ..models.subcategories import Subcategory
from ..models.categories import Category

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

        form=SubcategoryForm

        categories=Category.objects.all

        context = {
            'categories': categories,
            'form': form,
        }

        return render(request,'backend/subcategories/create.html',context)
    else:
        return render(request,'backend/auth/login.html')

#Store subcategory
def store(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            form = SubcategoryForm(request.POST)

            if form.is_valid():
                s = form.save(commit=False)
                s.created_at=timezone.now()
                s.updated_at=timezone.now()
                s.save()

                messages.success(request, 'Record saved successfully!')
                return HttpResponseRedirect('/app/subcategories/index')
            else:
                categories=Category.objects.all

                context = {
                    'categories': categories,
                    'form': form,
                }

                return render(request,'backend/subcategories/create.html',context)
        else:
            form=SubcategoryForm

            categories=Category.objects.all

            context = {
                'categories': categories,
                'form': form,
            }

            return render(request,'backend/subcategories/create.html',context)
    else:
        return HttpResponseRedirect('/app/login')