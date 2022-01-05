from django.urls import path,include
from store_app.views import store_view,product_detail



urlpatterns = [
    path('',store_view,name='store_link'),
    path('Category/<str:category_slug>',store_view,name='product_by_category_link'),
    path('Detail/<str:product_slug>',product_detail,name='product_detail_link')
]