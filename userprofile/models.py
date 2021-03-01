from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):

    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null=True)
    facebook=models.URLField(blank=True,null=True)
    twitter=models.URLField(blank=True,null=True)
    instagram=models.URLField(blank=True,null=True)
    profile_pic=models.ImageField(default='',blank=True, null=True, upload_to=f'profile_pics/{user.name}')

    def __str__(self):
        return self.name


