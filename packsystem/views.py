
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.views import generic
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache
from packsystem.utils.custom_decorators import custom_admin_only, custom_authorised_user

@custom_authorised_user
def welcome(request):
    return render(request, 'packsystem/dashboard.html', {})

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

@never_cache
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            print(f"the user is {user}")
            login(request, user)
            messages.success(request, "Successfully logged in")
            return HttpResponseRedirect('')
        else:
            messages.error(request, ("There was an error logging in, please try again...."))
    else: 
        return render(request, 'packsystem/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, ("you logged out"))
    return redirect("login")   
  



