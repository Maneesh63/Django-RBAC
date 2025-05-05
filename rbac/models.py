from django.db import models
from django.contrib.auth.models import User, AbstractUser
from rbac.permission_constants import Permissions
 

class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=50, unique=True, choices=Permissions.CHOICES)

    def __str__(self):
        return self.name

class GroupPermission(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group.name} - {self.permission.name}"

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group)


class product(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name