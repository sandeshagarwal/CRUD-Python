from django.contrib import admin
from  . models import User #check other way

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')
