from cart_app.models import Cart,CartItem
from cart_app.views import _cart_id


def cart_counter_data(request):
   cart_item_counter = 0
   if 'admin' in request.path:
      return {}
   else:
      try:
         cart = Cart.objects.get(cart_id=_cart_id(request))

         # cart_items = CartItem.objects.all().filter(user=request.user)

         cart_items = CartItem.objects.all().filter(cart=cart)
         for cart_item in cart_items:
            cart_item_counter += cart_item.quantity
      except Cart.DoesNotExist:
         cart_item_counter = 0
   return dict(cart_item_counter=cart_item_counter)




# my code
# def cart_counter_data(request):
#    cart_item_counter = 0
#    id = None
#    if 'admin' in request.path:
#       return {}
#    else:
#       try:
#          id = Cart.objects.get(cart_id =_cart_id(request))
#          items = CartItem.objects.all().filter(cart__cart_id=id)
#
#          for item in items:
#             cart_item_counter += item.quantity
#       except id.DoesNotExist or id is None:
#          cart_item_counter=0
#
#    return dict(cart_item_counter=cart_item_counter)

