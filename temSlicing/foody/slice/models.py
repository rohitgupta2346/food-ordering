from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass
class restourant(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')



class restourant_menu(models.Model):
    food_name=models.CharField(max_length=15)
    is_veg=models.BooleanField(default=True)
    price=models.IntegerField()
    restourant_id=models.ForeignKey(restourant,on_delete=models.CASCADE,related_name='restourant_id')


class order_details(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_id')
    food_id=models.ForeignKey(restourant_menu,on_delete=models.CASCADE,related_name='food_id')
    quantity=models.IntegerField()
    total_amount=models.IntegerField()
    status=models.CharField(max_length=40, default='order')





