from django.urls import path,include
from store_app.views import store_view



urlpatterns = [
    path('',store_view,name='store_link'),
    path('/<str:category_slug>',store_view,name='product_by_category_link')
]