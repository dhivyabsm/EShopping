from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=80)
    item_price = models.IntegerField()

    def __str__(self):
        return self.item_name

class Purchase(models.Model):
    purchase_id = models.IntegerField()
    purchase_details = models.CharField(max_length=90)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
    

    def __str__(self):
        return self.purchase_details

class Cart(models.Model):
    item_quantity = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.item)
   
class Customer(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=30)
    user_mobile_number = models.BigIntegerField()
    address = models.CharField(max_length=60)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ManyToManyField(Cart, blank=True)

    def __str__(self):
        return self.user_name

