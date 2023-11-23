from django.urls import path
from . import views

urlpatterns =[ 
    path('',views.welcome, name="dashboard"),
    path('orders/', views.orders, name="orders"),
    path('settings/', views.settings, name="settings"),
    path('clients/', views.clients, name="clients"),
    path('login/',views.login_user, name="login"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.logout_user, name="logout"),
]

