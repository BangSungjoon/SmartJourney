from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions, Answers, FinancialProduct


class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)

class ProductOptionSerializer(serializers.ModelSerializer):
    class OptionSerializer(serializers.ModelSerializer):
        class Meta:
            model = DepositOptions
            fields = '__all__'
    
    depositoptions_set = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = DepositProducts
        fields = '__all__'

class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'

class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('product',)

class SavingAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'
        read_only_fields = ('user',)

class SaveInvRatioSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialProduct
        fields = '__all__'
        # read_only_fields = ('user',)
