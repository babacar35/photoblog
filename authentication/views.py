from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
"""from django.contrib.messages import (  # Use django.contrib.messages for messages
    error,
    success,
)"""
# Create your views here.
def logout_user(request):
    logout(request)
    return redirect('login')

def login_page(request):
    form = LoginForm()
    messages= ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages = f'Hello {user.username} vous etes connecté'
                #success(request, f'Hello {user.username}! You are now logged in.')  # Use success message
                return redirect('home')
            else:
                messages = 'Username or password is incorrect'
                #error(request, 'Invalid username or password.')  # Use error message
                
    return render(request,'authentication/login.html',{
        'form': form,
        'messages': messages
    })