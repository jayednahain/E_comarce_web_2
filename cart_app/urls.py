from django.urls import path
from cart_app.views import cart_view,add_cart,remove_product_amount,remove_product

urlpatterns = [
    path('',cart_view,name='cart_view_link'),
    path('add_cart/<int:product_id>',add_cart,name='add_cart_link'),
    path('remove_amount/<int:product_id>/<int:cart_item_id>',remove_product_amount,name='remove_product_amount'),
    path('remove_cart_product/<int:product_id>/<int:cart_item_id>',remove_product,name='remove_cart_product')

]