
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
from django.contrib.auth.models import User
from .forms import AddUserForm
from uuid import UUID
from django.core.serializers.json import DjangoJSONEncoder


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        return super().default(obj)
    

@custom_authorised_user
def welcome(request):
    return render(request, 'packsystem/dashboard.html', {})

@custom_authorised_user
def orders(request):
    orders = Order.objects.all()
    data = {'orders': list(orders.values())}
    json_data = json.dumps(data, cls=DjangoJSONEncoder)
    print(json_data)

    context = {
        "orders": json_data,
        "section": "orders"
    }
    return render(request, 'packsystem/orders.html', context)

@custom_authorised_user
def add_order(request):
    # if request.method == 'POST':
    #     form = AddOrderForm(request.POST)
    #     # if form.is_valid():
    #     #     order = form.save(commit=False)
    #     #     order.save()
    #     #     messages.success(request, "Successfully added user")
    #     #     return HttpResponseRedirect('/orders')
    # else:
    #     # form = AddOrderForm()

    # return render(request, 'your_template.html', {'form': form})
    return render(request, 'packsystem/orders.html', {})

@custom_authorised_user
def edit_order(request):
    return render(request, 'packsystem/orders.html', {})

@custom_authorised_user
def add_user(request):
    username = request.user.username if request.user.is_authenticated else "Anonymous"
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added user")
            return HttpResponseRedirect('/clients')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                        messages.error(request, f"{error}")

        return HttpResponseRedirect('/clients')
    form = AddUserForm()
    # return render(request, 'packsystem/orders.html', {})


@custom_authorised_user
def settings(request):
    return render(request, 'packsystem/settings.html', {})

@custom_authorised_user
def clients(request):
    users = User.objects.all()
    usernames_list = [{"id": user.id, "username": user.username, "access_level": user.is_superuser} for user in users]
    data = {"users": usernames_list}
    print(data)
    context = {
         "users": json.dumps(data),
         "section": "users"
    }
    return render(request, 'packsystem/clients.html', context)

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
  



