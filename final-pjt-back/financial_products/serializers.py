from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions, Answers, FinancialProduct, ChangeMoney


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
        
 # 적금 옵션까지       
class SavingProductOptionsSerializer(serializers.ModelSerializer):
    class SavingOptionSerializer(serializers.ModelSerializer):
        class Meta:
            model = SavingOptions
            fields = '__all__'
    
    savingoptions_set = SavingOptionSerializer(many=True, read_only=True)

    class Meta:
        model = SavingProducts
        fields = '__all__'
    

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

class ChangeMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeMoney
        fields = '__all__'

# 작성자 정보가 포함된 포트폴리오 데이터를 만드는 serializer
class FinancialProductSerializer(serializers.ModelSerializer):
    # 작성자를 포함하기 위해 nested serializer 설정
    user = serializers.CharField(source='answer.user.username', read_only=True)
    user_id = serializers.IntegerField(source='answer.user.id', read_only=True)

    class Meta:
        model = FinancialProduct
        fields = '__all__'