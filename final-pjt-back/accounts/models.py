from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# class User(AbstractUser):
#     pass

class User(AbstractUser):
    deposit_products = models.ManyToManyField(
        'financial_products.DepositProducts',  # 연결할 상품 모델
        blank=True,
        related_name='users_with_deposit'
    )
    saving_products = models.ManyToManyField(
        'financial_products.SavingProducts',  # 연결할 상품 모델
        blank=True,
        related_name='users_with_saving'
    )