from django.db import models
from category_app.models import Category
from Utilities.media_path_convertor import upload_product_image_path
from django.urls import reverse
# Create your models here.


class Product(models.Model):
   product_name        = models.CharField(max_length=50,unique=True)
   slug                =  models.SlugField(unique=True,blank=True)
   product_description = models.TextField(max_length=100)
   price               = models.IntegerField()
   product_image       = models.ImageField(upload_to=upload_product_image_path)
   stock               = models.IntegerField()
   is_available        = models.BooleanField(default=True)
   category            = models.ForeignKey(Category,on_delete=models.CASCADE)
   create_date         = models.DateTimeField(auto_now_add=True)
   update_date         = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.product_name

   def get_absolute_url(self):
   #    # return 'detail/{slug}/'.format(slug=self.slug)
       return reverse('product_detail_link', kwargs={"slug": self.slug})