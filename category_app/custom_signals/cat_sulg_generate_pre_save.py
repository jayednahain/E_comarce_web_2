from django.db.models.signals import pre_save,post_save
from category_app.models import Category
from Utilities.slug_generator_with_signal import unique_slug_generator
from django.dispatch import receiver


@receiver(pre_save, sender=Category)
def category_slug_pre_save(sender,instance,*args,**kwargs):
   print(" categoru slug signal run! ! ")
   if not instance.slug:
      instance.slug = unique_slug_generator(instance)