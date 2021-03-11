from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class merchant(models.Model):
    shopkipper = models.ForeignKey(User, on_delete=models.CASCADE)
    shopname = models.CharField(max_length=200)

    def __str__(self):
        return self.shopkipper.username

class customers(models.Model):
    shopkipper = models.ForeignKey(User, on_delete=models.CASCADE)
    shopname = models.ForeignKey(merchant, on_delete=models.CASCADE)
    customername = models.CharField(max_length=200, default='unknown')
    selldetail = models.TextField(null=True, blank=True)
    dates = models.DateField(auto_now=True)
    selling = models.FloatField(default=0)

    def __str__(self):
        return self.shopkipper.username + '-' + 'selling data'