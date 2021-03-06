from django.db import models
from django.contrib.auth.models import User


class customerManager(models.Manager):
    def makeCustomer(self, user, zipCode, bio):
        customer = self.create(user=user, zipCode=zipCode, bio=bio)
        return customer

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    zipCode = models.IntegerField(default = '55555')
    bio = models.TextField(max_length = 1500)
    
    objects = customerManager()
    
    def __str__(self):
        return self.user.username
    

class customerServiceManager(models.Manager):
    def makeCustomerService(self, customer, servicesID):
        services = self.create(customer=customer, servicesID=servicesID, needsID="")
        return services
    
class CustomerService(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    servicesID = models.CharField(max_length = 600)
    needsID = models.CharField(max_length = 600)
    
    objects = customerServiceManager()
    
    def __str__(self):
        return self.customer.user.username