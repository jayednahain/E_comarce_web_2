from django.db import models
from Utilities.media_path_convertor import upload_category_image_path



class Category(models.Model):
   category_name    = models.CharField(max_length=50,unique=True)
   slug             = models.SlugField(blank=True,unique=True)
   cat_description  = models.TextField(max_length=100,blank=True)
   cat_image        = models.ImageField(upload_to=upload_category_image_path)
   cat_active       = models.BooleanField(default=True)
   cat_created_date = models.DateTimeField(auto_now_add=True)
   cat_update_date  = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.category_name

