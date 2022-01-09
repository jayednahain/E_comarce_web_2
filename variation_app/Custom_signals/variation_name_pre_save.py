from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from variation_app.models import Variation



@receiver(pre_save, sender=Variation)
def variation_pre_save(sender, instance, **kwargs):
   print("-----pre save signal run")
   if instance:
      instance.variation_name=instance.variation_name.lower()
   else:
      pass

