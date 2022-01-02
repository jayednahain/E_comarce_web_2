from django.shortcuts import render,get_object_or_404

from store_app.models import Product
from store_app.models import Category
# Create your views here.

def store_view(request,category_slug = None):
   categories = None
   product = None

   if category_slug is not None:
      categories = get_object_or_404(Category,slug = category_slug)
      product = Product.objects.filter(category =categories,is_available=True)
      total_product = product.count()
   else:
      product = Product.objects.all().filter(is_available=True)
      total_product = product.count()

   contenxt = {
      'all_product': product,
      'total_product':total_product
   }
   return render(request,'store.html',contenxt)