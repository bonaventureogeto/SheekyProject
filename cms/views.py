from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


#Home page
def index(request):
    return render(request, 'frontend/index.html')


#Salon
def salon(request):
    return render(request, 'frontend/salon.html')


#Barber
def barber(request):
    return render(request, 'frontend/barber.html')


#serviceCategories
def serviceCategories(request):
    return render(request, 'frontend/service_categories.html')


#serviceSubCategories
def serviceSubCategories(request):
    return render(request, 'frontend/service_subcategories.html')


#servicedetails
def serviceDetails(request):
    return render(request, 'frontend/service_details.html')


#myaccount
def myAccount(request):
    return render(request, 'frontend/myaccount.html')


#help
def help(request):
    return render(request, 'frontend/help.html')


#register
def register(request):
    return render(request, 'frontend/register.html')


#login
def login(request):
    """ view for login """
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')

        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    else:
        return render(request, 'frontend/login.html')
