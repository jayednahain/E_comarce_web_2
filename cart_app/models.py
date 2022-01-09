from django.db import models
from store_app.models import Product
# Create your models here.
from variation_app.models import Variation

class Cart(models.Model):
   cart_id = models.CharField(max_length=150,blank=True)
   created_date = models.DateField(auto_now_add=True)

   def __str__(self):
      return self.cart_id


class CartItem(models.Model):
   product = models.ForeignKey(Product,on_delete=models.CASCADE)
   variations = models.ManyToManyField(Variation,blank=True)
   cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
   quantity = models.IntegerField()
   is_active = models.BooleanField(default=True)

   def sub_total(self):
      return self.product.price * self.quantity


   def __unicode__(self):
      return self.product

   # def __str__(self):
   #    return self.product