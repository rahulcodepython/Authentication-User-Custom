from django.contrib import admin
from home.models import Custom_User

# Register your models here.

class User_admin(admin.ModelAdmin):
    model = "Custom_User"
    list_display = ['user', 'fathername', 'mothername', 'address', 'gender']

admin.site.register(Custom_User, User_admin)