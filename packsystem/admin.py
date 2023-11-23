from django.contrib import admin
from .models import PackageSystemUser, Order

admin.site.site_header = 'PACKAGE SYSTEM ADMINISTRATION'
admin.site.register(PackageSystemUser)
admin.site.register(Order)