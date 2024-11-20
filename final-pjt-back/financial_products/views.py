from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import requests
from .models import DepositOptions, DepositProducts, SavingProducts, SavingOptions
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, ProductOptionSerializer, SavingProductsSerializer, SavingOptionsSerializer, SavingAnswerSerializer
from rest_framework import status
from django.db.models import Max
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse



# Create your views here.
@api_view(['GET'])
def save_deposit(request):
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    for li in response.get('result')['baseList']:
        fin_prdt_cd= li['fin_prdt_cd']
        kor_co_nm= li['kor_co_nm']
        fin_prdt_nm= li['fin_prdt_nm']
        etc_note= li['etc_note']
        join_deny = li['join_deny']
        join_member = li['join_member']
        join_way = li['join_way']
        spcl_cnd = li['spcl_cnd']
    
        if DepositProducts.objects.filter(
            fin_prdt_cd=fin_prdt_cd,
            # kor_co_nm=kor_co_nm,
            # fin_prdt_nm=fin_prdt_nm,
            # etc_note=etc_note,
            # join_deny=join_deny,
            # join_member=join_member,
            # join_way=join_way,
            # spcl_cnd=spcl_cnd
            ):

            continue
    
        save_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny':join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd
        }
        serializer = DepositProductsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for li in response.get('result')['optionList']:

        fin_prdt_cd = li['fin_prdt_cd']
        intr_rate_type_nm = li['intr_rate_type_nm']
        intr_rate = li['intr_rate']
        intr_rate2 = li['intr_rate2']
        save_trm = li['save_trm']
        product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        print(fin_prdt_cd, intr_rate_type_nm, intr_rate, intr_rate2, save_trm, product)

        # 비어있는 필드에 대한 기본값 설정
        intr_rate_type_nm = li.get('intr_rate_type_nm', '-1')
        intr_rate = li.get('intr_rate', -1.0) if li.get('intr_rate') is not None else -1.0
        intr_rate2 = li.get('intr_rate2', -1.0) if li.get('intr_rate2') is not None else -1.0
        save_trm = li.get('save_trm', -1) if li.get('save_trm') is not None else -1


        if DepositOptions.objects.filter(
            fin_prdt_cd=fin_prdt_cd,
            intr_rate_type_nm=intr_rate_type_nm,
            intr_rate=intr_rate,
            intr_rate2=intr_rate2,
            save_trm=save_trm,
            product=product
        ):
            continue

        save_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate':intr_rate,
            'intr_rate2':intr_rate2,
            'save_trm':save_trm,
        }
        serializer = DepositOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
        
    return Response(response)


@api_view(['GET'])
def save_saving(request):
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    # return Response(response)
    for li in response.get('result')['baseList']:
        fin_prdt_cd= li['fin_prdt_cd']
        kor_co_nm= li['kor_co_nm']
        fin_prdt_nm= li['fin_prdt_nm']
        etc_note= li['etc_note']
        join_deny = li['join_deny']
        join_member = li['join_member']
        join_way = li['join_way']
        spcl_cnd = li['spcl_cnd']
    
        if SavingProducts.objects.filter(
            fin_prdt_cd=fin_prdt_cd,
            kor_co_nm=kor_co_nm,
            fin_prdt_nm=fin_prdt_nm,
            etc_note=etc_note,
            join_deny=join_deny,
            join_member=join_member,
            join_way=join_way,
            spcl_cnd=spcl_cnd):

            continue
    
        save_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny':join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd
        }
        serializer = SavingProductsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for li in response.get('result')['optionList']:

        fin_prdt_cd = li['fin_prdt_cd']
        intr_rate_type_nm = li['intr_rate_type_nm']
        intr_rate = li['intr_rate']
        intr_rate2 = li['intr_rate2']
        save_trm = li['save_trm']
        product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        print(fin_prdt_cd, intr_rate_type_nm, intr_rate, intr_rate2, save_trm, product)

        # 비어있는 필드에 대한 기본값 설정
        intr_rate_type_nm = li.get('intr_rate_type_nm', '-1')
        intr_rate = li.get('intr_rate', -1.0) if li.get('intr_rate') is not None else -1.0
        intr_rate2 = li.get('intr_rate2', -1.0) if li.get('intr_rate2') is not None else -1.0
        save_trm = li.get('save_trm', -1) if li.get('save_trm') is not None else -1


        if SavingOptions.objects.filter(
            fin_prdt_cd=fin_prdt_cd,
            intr_rate_type_nm=intr_rate_type_nm,
            intr_rate=intr_rate,
            intr_rate2=intr_rate2,
            save_trm=save_trm,
            product=product
        ):
            continue

        save_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate':intr_rate,
            'intr_rate2':intr_rate2,
            'save_trm':save_trm,
        }
        serializer = SavingOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
        
    return Response(response)

@api_view(['get'])
def get_depositproducts(request):
    bank = request.GET['bank'].split()[0]
    deposit_products = DepositProducts.objects.filter(kor_co_nm=bank).values()
    if deposit_products:
        response = {
            "deposit_products":list(deposit_products)
        }
        return JsonResponse(response)
    else:
        print("#######################################없음")


# 포트폴리오 비율 저장
@api_view(['post'])
@permission_classes([IsAuthenticated])
def save_answer(request):
    serializer = SavingAnswerSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)