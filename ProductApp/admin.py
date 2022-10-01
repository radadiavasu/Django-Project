from django.contrib import admin

from ProductApp.models import CategoryModel,ProductModel

# Register your models here.
#class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']
#   list_filter = ['name']
#admin.site.register(CategoryModel,CategoryAdmin)
admin.site.register(CategoryModel)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','description']
admin.site.register(ProductModel,ProductAdmin)