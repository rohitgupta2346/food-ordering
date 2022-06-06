from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to='images/')


class RestaurantMenu(models.Model):
    food_name = models.CharField(max_length=15)
    is_veg = models.BooleanField(default=True)
    price = models.IntegerField()
    menuImage = models.ImageField(upload_to="menuImages/", default="")
    restaurantId = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='RestaurantId')


class OrderDetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    food_id = models.ForeignKey(RestaurantMenu, on_delete=models.CASCADE, related_name='food_id')
    quantity = models.IntegerField()
    total_amount = models.IntegerField()
    status = models.CharField(max_length=40, default='order')


    def isApprove(self):
        if self.status == "APPROVED":
            return True
        else:
            return False

    def isRejected(self):
        if self.status == "REJECTED":
            return True
        else:
            return False
