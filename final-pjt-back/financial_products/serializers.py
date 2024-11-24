from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions, Answers, FinancialProduct, ChangeMoney, UserConditions, SupportServiceList
from datetime import datetime


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

# 사용자 조건 정보
class UserConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConditions
        fields = [
            'birth_year',
            'gender',
            'income_level',
            'is_expecting',
            'is_pregnant',
            'is_birth',
            'occupation',
            'student_status',
            'is_multicultural',
            'is_north_defector',
            'is_single_parent',
            'is_single_person',
            'is_many_children',
            'is_no_house',
            'is_new_resident',
            'business_status',
            'business_type',
            'is_disabled',
            'is_veteran',
            'is_patient'
        ]
        read_only_fields = ('user', 'created_at', 'updated_at')
        extra_kwargs = {
            'birth_year': {'required': True, 'min_value': 1},
            'gender': {'required': True},
            'income_level': {'required': True},
            'occupation': {'required': True},
        }

    def validate_birth_year(self, value):
        if not value or value <= 0:
            raise serializers.ValidationError("출생연도는 0보다 큰 숫자여야 합니다")
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("출생연도가 현재 연도보다 클 수 없습니다")
        return value

    def validate(self, data):
        required_fields = ['birth_year', 'gender', 'income_level', 'occupation']
        for field in required_fields:
            if field not in data or not data[field]:
                raise serializers.ValidationError(f"{field}는 필수 입력 항목입니다")
        return data

class SupportServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportServiceList
        fields = [
            'service_id',
            'support_type',
            'service_nm',
            'service_pur',
            'eligibility',
            'selection_criteria',
            'support_details',
            'application_method',
            'agency_name',
            'contact_number',
            'detail_url'
        ]