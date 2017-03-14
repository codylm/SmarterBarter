from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    zipCode = models.IntegerField(default = '55555')
    bio = models.TextField(max_length = 1500)
    
    def __str__(self):
        return self.user.username
    
class CustomerService(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    servicesID = models.CharField(max_length = 60)
    needsID = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.customer.user.username

    

