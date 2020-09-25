from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User


#register
def register(request):
    """
    Register user
    """
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        phone_no = request.POST['phone_no']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'The email is already registered')
                    return redirect('register')
                else:
                    # looks good
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(
                        request, 'You are now registered. You can proceed to login')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'frontend/accounts/register.html')


#login
def login(request):
    """ view for login """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('booking_page')

        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    else:
        return render(request, 'frontend/accounts/login.html')


#myaccount
def myaccount(request):
    customer = Customer.objects.all()

    context = {
        'customer': customer
    }

    return render(request, 'frontend/accounts/myaccount.html', context)


#register
def logout(request):
    return redirect('index')
