# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User
# # Register your models here.
# admin.site.register(User, UserAdmin)
# accounts/admin.py
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from financial_products.models import DepositProducts, SavingProducts

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['username']
    
    # ManyToManyField 필드를 관리하기 위한 설정
    filter_horizontal = ['deposit_products', 'saving_products']

admin.site.register(User, CustomUserAdmin)
