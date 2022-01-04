from django.shortcuts import render
from store_app.models import Product,Category
# Create your views here.


def home_page(request):
   all_category = Category.objects.all()
   all_product = Product.objects.all().filter(is_available=True)

   contenxt = {
      'all_product':all_product,
      'all_category': all_category
   }

   return render(request,'Home_page.html',contenxt)