from django.contrib import admin
from django.contrib.auth.models import User
from rbac.models import Group, Permission, GroupPermission, CustomUser, product


admin.site.register(Group)
admin.site.register(Permission)
admin.site.register(GroupPermission)
admin.site.register(CustomUser)
admin.site.register(product)