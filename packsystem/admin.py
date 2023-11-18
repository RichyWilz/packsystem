from django.contrib import admin
from .models import PackageSystemUser

admin.site.site_header = 'PACKAGE SYSTEM ADMINISTRATION'
admin.site.register(PackageSystemUser)