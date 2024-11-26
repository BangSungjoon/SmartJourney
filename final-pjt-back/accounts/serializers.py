from rest_framework import serializers
from .models import User
from financial_products.models import DepositProducts, SavingProducts

class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = ['id', 'fin_prdt_cd', 'kor_co_nm', 'fin_prdt_nm']

class SavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = ['id', 'fin_prdt_cd', 'kor_co_nm', 'fin_prdt_nm']

class UserSerializer(serializers.ModelSerializer):
    deposit_products = DepositProductSerializer(many=True, read_only=True)
    saving_products = SavingProductSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'deposit_products', 'saving_products']
