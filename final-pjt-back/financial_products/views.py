from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.conf import settings
import requests
from .models import DepositOptions, DepositProducts, SavingProducts, SavingOptions, Answers, FinancialProduct, ChangeMoney
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, ProductOptionSerializer, SavingProductsSerializer, SavingOptionsSerializer, SavingAnswerSerializer, SaveInvRatioSerializer, ChangeMoneySerializer, SavingProductOptionsSerializer
from rest_framework import status
from django.db.models import Max
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404



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
        # print(fin_prdt_cd, intr_rate_type_nm, intr_rate, intr_rate2, save_trm, product)

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
        rsrv_type_nm = li['rsrv_type_nm']
        intr_rate = li['intr_rate']
        intr_rate2 = li['intr_rate2']
        save_trm = li['save_trm']
        product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        # print(fin_prdt_cd, intr_rate_type_nm, intr_rate, intr_rate2, save_trm, product)

        # 비어있는 필드에 대한 기본값 설정
        intr_rate_type_nm = li.get('intr_rate_type_nm', '-1')
        intr_rate = li.get('intr_rate', -1.0) if li.get('intr_rate') is not None else -1.0
        intr_rate2 = li.get('intr_rate2', -1.0) if li.get('intr_rate2') is not None else -1.0
        save_trm = li.get('save_trm', -1) if li.get('save_trm') is not None else -1


        if SavingOptions.objects.filter(
            fin_prdt_cd=fin_prdt_cd,
            intr_rate_type_nm=intr_rate_type_nm,
            rsrv_type_nm = rsrv_type_nm,
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
            'rsrv_type_nm':rsrv_type_nm
        }
        serializer = SavingOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
        
    return Response(response)


@api_view(['GET'])
def save_deposit_savings(request):
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
        # print(fin_prdt_cd, intr_rate_type_nm, intr_rate, intr_rate2, save_trm, product)

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
        rsrv_type_nm = li['rsrv_type_nm']
        intr_rate = li['intr_rate']
        intr_rate2 = li['intr_rate2']
        save_trm = li['save_trm']
        product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        # print(fin_prdt_cd, intr_rate_type_nm, intr_rate, intr_rate2, save_trm, product)

        # 비어있는 필드에 대한 기본값 설정
        intr_rate_type_nm = li.get('intr_rate_type_nm', '-1')
        intr_rate = li.get('intr_rate', -1.0) if li.get('intr_rate') is not None else -1.0
        intr_rate2 = li.get('intr_rate2', -1.0) if li.get('intr_rate2') is not None else -1.0
        save_trm = li.get('save_trm', -1) if li.get('save_trm') is not None else -1


        if SavingOptions.objects.filter(
            fin_prdt_cd=fin_prdt_cd,
            intr_rate_type_nm=intr_rate_type_nm,
            rsrv_type_nm = rsrv_type_nm,
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
            'rsrv_type_nm':rsrv_type_nm
        }
        serializer = SavingOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
        
    return Response(response)





# 위치 마커 클릭하면 해당 은행의 정기 예금, 적금 상품 정보 추출
@api_view(['get'])
def get_depositproducts(request):
    bank = request.GET['bank'].split()[0]
    products = DepositProducts.objects.filter(kor_co_nm=bank).prefetch_related('depositoptions_set').all()
    if products:
        serializer = ProductOptionSerializer(products, many=True)
        return Response(serializer.data)
    else:
       return Response([], status=200)

# 예금 추천
@api_view(['get'])
def recommend_deposit(request):
    bank = request.GET['bank']
    products = DepositProducts.objects.filter(kor_co_nm=bank).prefetch_related('depositoptions_set').all()
    if products:
        serializer = ProductOptionSerializer(products, many=True)
        return Response(serializer.data)
    else:
       return Response([], status=200)
   
# 적금 추천
@api_view(['get'])
def recommend_savings(request):
    bank = request.GET['bank']
    products = SavingProducts.objects.filter(kor_co_nm=bank).prefetch_related('savingoptions_set').all()
    if products:
        serializer = SavingProductOptionsSerializer(products, many=True)
        return Response(serializer.data)
    else:
       return Response([], status=200)
    


# 예금 추천 상세
@api_view(['get'])
def recommend_deposit_datail(request):
    fincode = request.GET['fincode']
    products = DepositProducts.objects.filter(fin_prdt_cd=fincode).prefetch_related('depositoptions_set').all()
    if products:
        serializer = ProductOptionSerializer(products, many=True)
        return Response(serializer.data)
    else:
       return Response([], status=200)


# 적금 추천 상세
@api_view(['get'])
def recommend_savings_detail(request):
    fincode = request.GET['fincode']
    products = SavingProducts.objects.filter(fin_prdt_cd=fincode).prefetch_related('savingoptions_set').all()
    if products:
        serializer = SavingProductOptionsSerializer(products, many=True)
        return Response(serializer.data)
    else:
       return Response([], status=200)


# 포트폴리오 비율 저장
@api_view(['post'])
@permission_classes([IsAuthenticated])
def save_answer(request):
    serializer = SavingAnswerSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['post'])
@permission_classes([IsAuthenticated])
def save_ratio(request, answer_id): 
    answer = get_object_or_404(Answers, pk=answer_id)
    save_inv_serializer = SaveInvRatioSerializer(data=request.data)
    if save_inv_serializer.is_valid(raise_exception=True):
        save_inv_serializer.save(answer=answer)
        return Response(save_inv_serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['get'])
@permission_classes([IsAuthenticated])
def my_portfolios(request, user_id):
    # 해당 user_id를 가진 모든 Answers 객체를 조회한다.
    answers = Answers.objects.filter(user_id=user_id)

    if not answers.exists():
        return Response({'detail': 'No answers found for this user.'}, status=404)
    
    # Answers 객체에 연결된 모든 FinancialProduct 객체를 가져온다.
    financial_products = []
    for answer in answers:
        try:
            financial_product = FinancialProduct.objects.get(answer=answer)
            financial_products.append(financial_product)
        except FinancialProduct.DoesNotExist:
            continue # 해당 Answers에 연결된 FinancialProduct가 없다면 그냥 넘어가기

    # FinancialProduct 객체들을 직렬화하여 반환하기
    if financial_products:
        serializer = SaveInvRatioSerializer(financial_products, many=True)
        return Response(serializer.data)
    else:
        return Response({"detail": "No financial products found for these answers."}, status=404)

# 해당 날짜 환률 정보를 받아오고 DB에 저장하는 작업   
@api_view(['GET'])
def change_money(request):
    api_key = settings.AUTH_KEY
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&data=AP01'

    response = requests.get(url, verify=False)
    response.raise_for_status()  # HTTP 에러 발생 시 예외 처리
    data = response.json()  # JSON 응답 데이터를 Python 리스트로 변환
    if data:                # 데이터가 있을 때만 DB갱신 오늘 날짜 기준 오전 11시 이전엔 빈배열이 올 수 있음
        for li in data:
            if li['result'] == 1:   # 조회 결과가 성공일때만 DB 갱신
                cur_unit = li['cur_unit']
                ttb = li['ttb']
                tts = li['tts']
                deal_bas_r = li['deal_bas_r']
                cur_nm = li['cur_nm']

                # 동일한 정보가 DB에 있다면, 넘어갑시다!
                if ChangeMoney.objects.filter(
                    cur_unit=cur_unit,
                    ttb=ttb,
                    tts=tts,
                    deal_bas_r=deal_bas_r,
                    cur_nm=cur_nm
                ):
                    continue
                # 동일한 cur_unit 데이터 삭제
                ChangeMoney.objects.filter(cur_unit=cur_unit).delete()

                # serializer 사용해서 데이터 저장
                save_data = {
                    'cur_unit': cur_unit,
                    'ttb': ttb,
                    'tts': tts,
                    'deal_bas_r': deal_bas_r,
                    'cur_nm': cur_nm
                }
                serializer = ChangeMoneySerializer(data=save_data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()

    return Response(data)

# DB에 저장된 환률 정보를 반환하는 함수
# DB에 저장과 반환을 동시에 하지 않는 이유는 환률정보 API 호출 제한이 있기 때문에 따로 수행
@api_view(['GET'])
def exchange(request):
    money = ChangeMoney.objects.all()
    serializer = ChangeMoneySerializer(money, many=True)
    return Response(serializer.data)


# 포트폴리오를 삭제할 수 있는 DELETE 요청
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_portfolio(request, portfolio_id):
    try:
        portfolio = FinancialProduct.objects.get(pk=portfolio_id)
        if portfolio.answer.user != request.user:
            return Response({"error": "권환이 없습니다."}, status=403)
        portfolio.delete()
        return Response({"message": "포트폴리오가 삭제되었습니다."}, status=200)
    except FinancialProduct.DoesNotExist:
        return Response({"error": "해당 포트폴리오를 찾을 수 없습니다."}, status=404)
    
from .serializers import FinancialProductSerializer

@api_view(['GET'])
def get_user_portfolios(request, user_id):
    # 해당 user_id로 작성된 포트폴리오 가져오기
    portfolios = FinancialProduct.objects.filter(answer__user__id=user_id)
    serializer = FinancialProductSerializer(portfolios, many=True)
    return Response(serializer.data)

############### 보조금 찾기 ###############
@api_view(['GET'])
def subsidy_list_save(request):
    api_key = settings.SUBSIDY_KEY
    for page in range(1, 102):
        url = f'https://api.odcloud.kr/api/gov24/v3/serviceList?page={page}&serviceKey={api_key}&perPage=100'
        response = requests.get(url)
        data = response.json()  # JSON 응답 데이터를 Python 리스트로 변환
        # print(data['data'][0])
        # for li in data['data']:

    
    # if data:                # 데이터가 있을 때만 DB갱신 오늘 날짜 기준 오전 11시 이전엔 빈배열이 올 수 있음
    #     for li in data:
    #         if li['result'] == 1:   # 조회 결과가 성공일때만 DB 갱신
    #             cur_unit = li['cur_unit']
    #             ttb = li['ttb']
    #             tts = li['tts']
    #             deal_bas_r = li['deal_bas_r']
    #             cur_nm = li['cur_nm']

    #             # 동일한 정보가 DB에 있다면, 넘어갑시다!
    #             if ChangeMoney.objects.filter(
    #                 cur_unit=cur_unit,
    #                 ttb=ttb,
    #                 tts=tts,
    #                 deal_bas_r=deal_bas_r,
    #                 cur_nm=cur_nm
    #             ):
    #                 continue
    #             # 동일한 cur_unit 데이터 삭제
    #             ChangeMoney.objects.filter(cur_unit=cur_unit).delete()

    #             # serializer 사용해서 데이터 저장
    #             save_data = {
    #                 'cur_unit': cur_unit,
    #                 'ttb': ttb,
    #                 'tts': tts,
    #                 'deal_bas_r': deal_bas_r,
    #                 'cur_nm': cur_nm
    #             }
    #             serializer = ChangeMoneySerializer(data=save_data)
    #             if serializer.is_valid(raise_exception=True):
    #                 serializer.save()

    return Response(data)