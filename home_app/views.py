from django.shortcuts import render
from store_app.models import Product
# Create your views here.


def home_page(request):
   all_product = Product.objects.all().filter(is_available=True)

   contenxt = {
      'all_product':all_product
   }

   return render(request,'Home_page.html',contenxt)