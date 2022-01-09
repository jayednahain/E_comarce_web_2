from django.db import models
from store_app.models import Product
from category_app.models import Category

from variation_app.custom_variation_manager.variation_manager import VariationManager
# Create your models here.


variation_choise = (
   ('color','color'),
   ('size','size')
)


class Variation(models.Model):
   product = models.ForeignKey(Product,on_delete=models.CASCADE)
   variation_category = models.CharField(max_length=80,choices=variation_choise)
   variation_name = models.CharField(max_length=30)
   is_active = models.BooleanField(default=True)
   created_date = models.DateTimeField(auto_now_add=True)
   update_time = models.DateTimeField(auto_now=True)
   objects     =VariationManager()

   def __str__(self):
      return self.variation_name

