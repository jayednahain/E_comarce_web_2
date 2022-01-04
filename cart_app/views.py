from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from store_app.models import Product
from cart_app.models import Cart, CartItem
from category_app.models import Category

"""
session id will be the cart id
 
"""


def _cart_id(request):
   cart = request.session.session_key
   if not cart:
      cart = request.session.create()
   return cart


"""it will add single item to the cart"""


def add_cart(request, product_id):
   print(product_id)
   product_instance = Product.objects.get(id=product_id)

   """get current cart id"""
   try:
      cart = Cart.objects.get(cart_id=_cart_id(request))
   except Cart.DoesNotExist:
      cart = Cart.objects.create(
         cart_id=_cart_id(request)
      )
   cart.save()

   """items inside the cart"""
   try:
      cart_item_instance = CartItem.objects.get(product=product_instance, cart=cart)
      cart_item_instance.quantity += 1
      cart_item_instance.save()
   except CartItem.DoesNotExist:
      cart_item_instance = CartItem.objects.create(
         product=product_instance,
         quantity=1,
         cart=cart
      )
      cart_item_instance.save()
   return redirect('cart_view_link')


def remove_product_amount(request,product_id):
   cart_instance= Cart.objects.get(cart_id=_cart_id(request))
   product_instance = get_object_or_404(Product,id=product_id)
   cart_item_instance = CartItem.objects.get(product=product_instance,cart=cart_instance)

   if cart_item_instance.quantity > 1:
      cart_item_instance.quantity -=1
      cart_item_instance.save()
   else:
      cart_item_instance.delete()

   return redirect('cart_view_link')

def remove_product(request,product_id):
   cart_instance = Cart.objects.get(cart_id=_cart_id(request))
   product_instance = get_object_or_404(Product,id=product_id)
   cart_item_instance = CartItem.objects.get(product=product_instance,cart=cart_instance)
   cart_item_instance.delete()

   return redirect('cart_view_link')




def cart_view(request,total = 0, quantity=0,cart_items_instance=None):
   all_Category = Category.objects.all()
   tax=0
   grand_total=0
   try:
      cart_instance = Cart.objects.get(cart_id=_cart_id(request))
      cart_items_instance = CartItem.objects.filter(
         cart = cart_instance,
         is_active=True
      )
      for cart_item in cart_items_instance:
         total += (cart_item.product.price * cart_item.quantity)
         quantity +=cart_item.quantity
      #2% tax
      tax = (2*total)/100
      grand_total = total+tax

   except ObjectDoesNotExist:
      pass

   context={
      'total':total,
      'quantity':quantity,
      'cart_items':cart_items_instance,
      'tax':tax,
      'grand_total':grand_total,
      'all_category':all_Category

   }

   return render(request, 'cart.html',context)

def test(request):
   cart_obj = Cart.objects.filter(cart_id='xh6arfwgzj6hh1ss5gmbuzcay6394wwc')
   cart_items_obj = CartItem.objects.filter(cart__cart_id=cart_obj)

   return
