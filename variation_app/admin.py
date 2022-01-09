from django.contrib import admin
from variation_app.models import Variation
# Register your models here.

class AdminVariation(admin.ModelAdmin):
   list_display = ['product','variation_category','variation_name','is_active']
   list_editable = ('is_active',)
   list_filter = ('product','variation_category','variation_name','is_active')
admin.site.register(Variation,AdminVariation)
