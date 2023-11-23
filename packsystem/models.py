from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

# Create your models here.
class PackageSystemUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Order(models.Model):
    orderId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    delivery_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20)

    def __str__(self):
        return [self.orderId, self.name]

