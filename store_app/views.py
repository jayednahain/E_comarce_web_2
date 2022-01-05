from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

from store_app.models import Product
from store_app.models import Category
from cart_app.views import _cart_id
from cart_app.models import CartItem
# Create your views here.

def store_view(request,category_slug = None):
   categories = None
   product = None
   all_category = Category.objects.all()

   if category_slug is not None:
      categories = get_object_or_404(Category,slug = category_slug)
      product = Product.objects.filter(category =categories,is_available=True)
      total_product = product.count()

      """pagination"""
      page_number = request.GET.get('page', None)
      if total_product==1:
         display_item = total_product
      else:
         display_item =total_product-1
      paginator = Paginator(product, display_item)
      display_product = paginator.get_page(page_number)


   else:
      product = Product.objects.all().filter(is_available=True)
      total_product = product.count()

      """pagination"""
      page_number = request.GET.get('page',None)
      print(page_number)
      #display_item=6
      paginator = Paginator(product,6)
      display_product = paginator.get_page(page_number)
      

   contenxt = {
      'all_product': display_product,
      'total_product':total_product,
      'all_category':all_category
   }
   return render(request,'store.html',contenxt)


def product_detail(request,product_slug):
   all_category = Category.objects.all()
   try:
      product_instance = Product.objects.get(slug__exact=product_slug)
      """check the product is already in cart or not
      """
      cart_instance = CartItem.objects.filter(
         cart__cart_id=_cart_id(request),
         product=product_instance
      ).exists()
   except Exception as e:
      raise e
   contenxt ={
      'cart_check':cart_instance,
      'product_data':product_instance,
      'all_category': all_category
   }
   return render(request,'prodcut_detail.html',contenxt)

