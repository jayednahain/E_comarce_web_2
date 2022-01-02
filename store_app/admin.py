from django.contrib import admin
from store_app.models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
   list_display = ('product_name','price','stock','category','create_date')


admin.site.register(Product,ProductAdmin)

