
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.views import generic
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache
from packsystem.utils.custom_decorators import custom_admin_only, custom_authorised_user
from .models import Order
import json

@custom_authorised_user
def welcome(request):
    return render(request, 'packsystem/dashboard.html', {})

@custom_authorised_user
def orders(request):
    orders = Order.objects.all()
    orders_list = [{"orderId": order.orderId, "name": order.name, "client": order.client,
                    "receiver": order.receiver, "delivery_date": order.delivery_date, "status": order.status}
                   for order in orders]
    data  = {"orders": orders_list}
    context = {
        "orders": json.dumps(data),
        "section": "orders"
    }
    return render(request, 'packsystem/orders.html', context)

@custom_authorised_user
def add_order(request):
    return render(request, 'packsystem/orders.html', {})


@custom_authorised_user
def settings(request):
    return render(request, 'packsystem/settings.html', {})

@custom_authorised_user
def clients(request):
    return render(request, 'packsystem/clients.html', {})

@custom_authorised_user
def activity(request):
    return render(request, 'packsystem/activity.html', {})

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
            return HttpResponseRedirect('/')
        else:
            messages.error(request, ("There was an error logging in, please try again...."))
            return render(request, 'packsystem/login.html',{})
    else: 
        return render(request, 'packsystem/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, ("you logged out"))
    return redirect("login")  

def display_message(message):
    escaped_message = html.escape(message)
    print("<script>alert('" + escaped_message + "');</script>")

    message = input("Enter your message: ")
    display_message(message) 
  



