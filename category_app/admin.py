from django.contrib import admin
from category_app.models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
   list_display = ('category_name','cat_created_date','slug')


admin.site.register(Category,CategoryAdmin)

