from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PackageSystemUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Order(models.Model):
    orderId = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    delivery_date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name

