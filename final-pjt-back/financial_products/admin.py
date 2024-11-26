# financial_products/admin.py
from django.contrib import admin
from .models import DepositProducts, SavingProducts

admin.site.register(DepositProducts)
admin.site.register(SavingProducts)

