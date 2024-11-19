from django.db import models
from django.conf import settings

# Create your models here.
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()

class DepositOptions(models.Model):
    product = models.ForeignKey("financial_products.DepositProducts", on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()

class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    etc_note = models.TextField()

class SavingOptions(models.Model):
    product = models.ForeignKey("financial_products.SavingProducts", on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()


################# 포트폴리오 모델 ####################

class Answers(models.Model):    # 답변 기록
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    q1_expected_goal_amount = models.IntegerField() # 목표를 달성하기 위해 필요한 예상 금액
    q2_goal_duration = models.IntegerField()   # 목표를 언제까지 달성하고 싶으신가요?
    q3_income_source = models.IntegerField()   # 현재 소득은 어떻게 얻고 있나요?
    q4_emergency_fund_status = models.IntegerField()   # 예기치 않은 상황에 대비한 비상 자금이 마련되어 있나요?
    q5_investment_priority = models.IntegerField() # 투자할 때 더 중요하게 여기는 것
    q6_safety_or_liquidity = models.IntegerField() # 안전성과 유동성 중 중요한 부분
    q7_household_status = models.IntegerField()    # 가계 상황
    q8_average_monthly_income = models.IntegerField()  # 평균적인 월 수입

class PortRisk(models.Model):  # 위험도에 따른 분류
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)
    # 위험도에 따른 포폴 구성 비율 저장 필드
    low_ratio = models.IntegerField()
    med_low_ratio = models.IntegerField()
    med_ratio = models.IntegerField()
    med_high_ratio = models.IntegerField()
    high_ratio = models.IntegerField()

class SaveInvType(models.Model):  # 자산 유형(저축 / 투자)에 따른 분류
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)
    # 자산 유형(저축 / 투자)에 따른 포폴 구성 비율 저장 필드
    saving_ratio = models.IntegerField()    
    inv_ratio = models.IntegerField()

class PortInvType(models.Model): # 자산 유형(투자 상품 내)에 따른 분류
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)
    # 자산 유형(투자 상품 내)에 따른 포폴 구성 비율 저장 필드
    dom_stock_ratio = models.IntegerField()   # 국내 주식형
    int_stock_ratio = models.IntegerField()   # 해외 주식형
    bond_ratio = models.IntegerField()    # 채권형
    alt_invest_ratio = models.IntegerField()  # 대안투자


class PortSaveType(models.Model): # 자산 유형(저축 상품 내)에 따른 분류
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)
    # 자산 유형(저축 상품 내)에 따른 포폴 구성 비율 저장 필드
    inst_save_ratio = models.IntegerField() 
    reg_save_ratio = models.IntegerField() 