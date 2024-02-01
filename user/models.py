from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Role(models.Model):
    id=models.AutoField(primary_key=True)
    role = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='roles', blank=True)
    
    def __str__(self):
        return self.role
    
class Permission(models.Model):
    modules = models.ManyToManyField('Module', related_name='permissions')
    roles = models.ManyToManyField('Role',max_length=255)

    def __str__(self):
        role_name= ', '.join(str(role) for role in self.roles.all())
        return f"permission for role: {role_name}"
    
class Module(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.name