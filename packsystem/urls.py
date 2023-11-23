from django.urls import path
from . import views

urlpatterns =[ 
    # path('',views.welcome, name="dashboard"),
    path('', views.orders, name="orders"),
    path('settings/', views.settings, name="settings"),
    path('clients/', views.clients, name="clients"),
    path('activity/', views.activity, name="activity"),
    path('add_order/', views.add_order, name="add_order"),
    path('add_user/', views.add_user, name="add_user"),
    path('edit_order/<int:ip_id>/', views.edit_order, name="edit_order"),
    path('login/',views.login_user, name="login"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.logout_user, name="logout"),
]

