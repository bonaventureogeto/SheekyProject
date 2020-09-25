from django.shortcuts import render
from django.contrib.auth import authenticate, login as admin_login
from django.contrib.auth import logout as logout_admin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

#Show admin login form
def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/app/dashboard')
    else:
        return render(request,'backend/auth/login.html')

#Authenticate admin
def autheticate(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        admin_login(request, user)
        # Redirect to a success page?
        return HttpResponseRedirect('/app/dashboard')
    else:
        #context = {'error': 'Wrong credintials'}  # to display error?
        #return render(request, 'backend/auth/login.html', {'context': context})
        return render(request, 'backend/auth/login.html', {
            'error_message': "Invalid username or password!",
        })

#Logout admin
@login_required
def logout(request):
    logout_admin(request)
    return HttpResponseRedirect('/app/login')

#Show admin dashboard
def index(request):
    if request.user.is_authenticated:
        return render(request, 'backend/dashboard.html')
    else:
        return render(request,'backend/auth/login.html')