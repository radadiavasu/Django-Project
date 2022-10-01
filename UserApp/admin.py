from django.contrib import admin

from UserApp.models import UserModel

#Register your models here.
class UserAdmin(admin.ModelAdmin):
   list_display = ['name','email','contact'] 
   list_filter=['contact','email']
admin.site.register(UserModel,UserAdmin)
#admin.site.register(UserModel)
