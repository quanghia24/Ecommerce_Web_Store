from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.conf import settings
from django.db.models import Sum
from django.shortcuts import reverse
# from django_countries.fields import CountryField


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

# Item on display
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    #"""A "slug" is a way of generating a valid URL, generally using data already obtained. For instance, a slug uses the title of an article to generate a URL. I advise to generate the slug by means of a function, given the title (or another piece of data), rather than setting it manually."""

    def __str__(self):
        return self.title

# Item in cart
class OrderItem(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price


# shopping cart: store all the item user have wishlisted
class Order(models.Model):
    # currently using User model from REST framework
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    items = models.ManyToManyField(OrderItem)
    ref_code = models.CharField(max_length=20, blank=True, null=True)

    start_date = models.DateTimeField(auto_now_add=True) 
    ordered_date = models.DateTimeField()
    
    ordered = models.BooleanField(default=False)



    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
            
        return total

