from django.db.models.signals import pre_save,post_save
from store_app.models import Product
from Utilities.product_slug_generator import product_unique_slug_generator
from django.dispatch import receiver


@receiver(pre_save, sender=Product)
def product_slug_pre_save(sender,instance,*args,**kwargs):
   print(" product slug signal run! ! ")
   if not instance.slug:
      instance.slug = product_unique_slug_generator(instance)