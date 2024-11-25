from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.conf import settings
import requests
from .models import DepositOptions, DepositProducts, SavingProducts, SavingOptions, Answers, FinancialProduct, ChangeMoney, SupportServiceList, SupportServiceDetail, SupportConditions, UserConditions
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, ProductOptionSerializer, SavingProductsSerializer, SavingOptionsSerializer, SavingAnswerSerializer, SaveInvRatioSerializer, ChangeMoneySerializer, SavingProductOptionsSerializer, UserConditionsSerializer, SupportServiceListSerializer
from rest_framework import status
from django.db.models import Max
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q




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
# 보조금 서비스 리스트
@api_view(['GET'])
def subsidy_list_save(request):
    api_key = settings.SUBSIDY_KEY
    for page in range(1, 102):
        url = f'https://api.odcloud.kr/api/gov24/v3/serviceList?page={page}&serviceKey={api_key}&perPage=100'
        response = requests.get(url)
        data = response.json()  # JSON 응답 데이터를 Python 리스트로 변환
        # print(data['data'][0])
        for li in data['data']:
            service = SupportServiceList(
                service_id=li['서비스ID'],  # 기본 키
                support_type=li['지원유형'],
                service_nm=li['서비스명'],
                service_pur=li['서비스목적요약'],
                eligibility=li['지원대상'],
                selection_criteria=li['선정기준'],
                support_details=li['지원내용'],
                application_method=li['신청방법'],
                application_deadline=li.get('신청기한', None),
                detail_url=li['상세조회URL'],
                agency_code=li['소관기관코드'],
                agency_name=li['소관기관명'],
                part_nm=li.get('부서명', None),
                agency_type=li['소관기관유형'],
                user_class=li['사용자구분'],
                service_class=li['서비스분야'],
                reception_agency=li.get('접수기관', None),
                contact_number=li.get('전화문의', None),
            )
            service.save()

    return Response(data)

# 보조금 서비스 디테일
@api_view(['GET'])
def subsidy_detail_save(request):
    api_key = settings.SUBSIDY_KEY
    for page in range(1, 102):
        url = f'https://api.odcloud.kr/api/gov24/v3/serviceDetail?page={page}&serviceKey={api_key}&perPage=100'
        response = requests.get(url)
        data = response.json()  # JSON 응답 데이터를 Python 리스트로 변환
        for li in data['data']:
            service = SupportServiceDetail(
                service = get_object_or_404(SupportServiceList, pk=li['서비스ID']),
                document=li.get('구비서류', None),
                apply_url=li.get('온라인청사이트URL', None),
                update_date=li.get('수정일시', None),
            )
            service.save()

    return Response(data)

# 보조금 지원 조건
@api_view(['GET'])
def support_conditions_save(request):
    api_key = settings.SUBSIDY_KEY
    for page in range(1, 102):
        url = f'https://api.odcloud.kr/api/gov24/v3/supportConditions?page={page}&serviceKey={api_key}&perPage=100'
        response = requests.get(url)
        data = response.json()
        
        for li in data['data']:
            service_id = li['서비스ID']
            
            # 'Y' 값을 Boolean으로 변환하는 함수
            def is_condition_true(value):
                return value == 'Y'
            
            try:
                condition = SupportConditions.objects.get(service_id=service_id)
                
                # 데이터 업데이트를 위한 새로운 데이터 준비
                updated_data = {
                    'is_male': is_condition_true(li.get('JA0101')),         # 남성
                    'is_female': is_condition_true(li.get('JA0102')),       # 여성
                    'age_start': li.get('JA0110'),                        # 나이 시작
                    'age_end': li.get('JA0111'),                            # 나이 끝
                    'income_0_50': is_condition_true(li.get('JA0201')),      # 소득 0~50%
                    'income_51_75': is_condition_true(li.get('JA0202')),   # 소득 51~75%
                    'income_76_100': is_condition_true(li.get('JA0203')),  # 소득 76~100%
                    'income_101_200': is_condition_true(li.get('JA0204')), # 소득 101~200%
                    'income_over_200': is_condition_true(li.get('JA0205')), # 소득 200% 초과
                    'is_expecting': is_condition_true(li.get('JA0301')),   # 예비부모/난임
                    'is_pregnant': is_condition_true(li.get('JA0302')),    # 임산부
                    'is_birth': is_condition_true(li.get('JA0303')),       # 출산
                    'is_farmer': is_condition_true(li.get('JA0313')),      # 농업
                    'is_fisher': is_condition_true(li.get('JA0314')),      # 어업
                    'is_livestock': is_condition_true(li.get('JA0315')),   # 축산업
                    'is_forester': is_condition_true(li.get('JA0316')),   # 임업인
                    'is_elementary': is_condition_true(li.get('JA0317')),  # 초등학생
                    'is_middle': is_condition_true(li.get('JA0318')),      # 중학생
                    'is_high': is_condition_true(li.get('JA0319')),       # 고등학생
                    'is_college': is_condition_true(li.get('JA0320')),      # 대학생
                    'is_employed': is_condition_true(li.get('JA0326')),      
                    'is_unemployed': is_condition_true(li.get('JA0327')),     
                    'is_multicultural': is_condition_true(li.get('JA0401')), # 다문화
                    'is_north_defector': is_condition_true(li.get('JA0402')), # 북한이탈주민
                    'is_single_parent': is_condition_true(li.get('JA0403')), # 한부모
                    'is_single_person': is_condition_true(li.get('JA0404')), # 1인가구
                    'is_many_children': is_condition_true(li.get('JA0411')), # 다자녀
                    'is_no_house': is_condition_true(li.get('JA0412')),    # 무주택자
                    'is_new_resident': is_condition_true(li.get('JA0413')),  # 신규전입
                    'is_extended_family': is_condition_true(li.get('JA0414')), # 가족형태
                    'is_prospective': is_condition_true(li.get('JA1101')),   # 예비부모
                    'is_in_operation': is_condition_true(li.get('JA1102')),   # 운영중
                    'is_closing': is_condition_true(li.get('JA1103')),       # 폐업
                    'is_food_business': is_condition_true(li.get('JA1201')),  # 식품업
                    'is_manufacturing': is_condition_true(li.get('JA1202')),  # 제조업
                    'is_other_business': is_condition_true(li.get('JA1299')),  # 기타업종
                    'is_small_business': is_condition_true(li.get('JA2101')), # 중소기업
                    'is_social_welfare': is_condition_true(li.get('JA2102')),
                    'is_organization': is_condition_true(li.get('JA2103')),
                    'is_corp_manufacturing': is_condition_true(li.get('JA2201')),
                    'is_corp_agriculture': is_condition_true(li.get('JA2202')),
                    'is_corp_it': is_condition_true(li.get('JA2203')),
                    'is_corp_other': is_condition_true(li.get('JA2299')),
                    'is_disabled': is_condition_true(li.get('JA0328')),
                    'is_veteran': is_condition_true(li.get('JA0329')),
                    'is_patient': is_condition_true(li.get('JA0330'))
                }
                
                # 현재 데이터와 비교하여 변경사항이 있는지 확인
                has_changes = False
                for key, value in updated_data.items():
                    if getattr(condition, key) != value:
                        has_changes = True
                        break
                
                # 변경사항이 있을 경우에만 업데이트
                if has_changes:
                    for key, value in updated_data.items():
                        setattr(condition, key, value)
                    condition.save()
                    
            except SupportConditions.DoesNotExist:
                # 새로운 데이터 생성
                try:
                    service = SupportServiceList.objects.get(service_id=service_id)
                    condition = SupportConditions(
                        service=service,
                        is_male=is_condition_true(li.get('JA0101')),
                        is_female=is_condition_true(li.get('JA0102')), 
                        age_start=li.get('JA0110'),
                        age_end=li.get('JA0111'),
                        income_0_50=is_condition_true(li.get('JA0201')),
                        income_51_75=is_condition_true(li.get('JA0202')),
                        income_76_100=is_condition_true(li.get('JA0203')),
                        income_101_200=is_condition_true(li.get('JA0204')),
                        income_over_200=is_condition_true(li.get('JA0205')),
                        is_expecting=is_condition_true(li.get('JA0301')),
                        is_pregnant=is_condition_true(li.get('JA0302')),
                        is_birth=is_condition_true(li.get('JA0303')),
                        is_farmer=is_condition_true(li.get('JA0313')),
                        is_fisher=is_condition_true(li.get('JA0314')),
                        is_livestock=is_condition_true(li.get('JA0315')),
                        is_forester=is_condition_true(li.get('JA0316')),
                        is_elementary=is_condition_true(li.get('JA0317')),
                        is_middle=is_condition_true(li.get('JA0318')),
                        is_high=is_condition_true(li.get('JA0319')),
                        is_college=is_condition_true(li.get('JA0320')),
                        is_employed=is_condition_true(li.get('JA0326')),
                        is_unemployed=is_condition_true(li.get('JA0327')),
                        is_multicultural=is_condition_true(li.get('JA0401')),
                        is_north_defector=is_condition_true(li.get('JA0402')),
                        is_single_parent=is_condition_true(li.get('JA0403')),
                        is_single_person=is_condition_true(li.get('JA0404')),
                        is_many_children=is_condition_true(li.get('JA0411')),
                        is_no_house=is_condition_true(li.get('JA0412')),
                        is_new_resident=is_condition_true(li.get('JA0413')),
                        is_extended_family=is_condition_true(li.get('JA0414')),
                        is_prospective=is_condition_true(li.get('JA1101')),
                        is_in_operation=is_condition_true(li.get('JA1102')),
                        is_closing=is_condition_true(li.get('JA1103')),
                        is_food_business=is_condition_true(li.get('JA1201')),
                        is_manufacturing=is_condition_true(li.get('JA1202')),
                        is_other_business=is_condition_true(li.get('JA1299')),
                        is_small_business=is_condition_true(li.get('JA2101')),
                        is_social_welfare=is_condition_true(li.get('JA2102')),
                        is_organization=is_condition_true(li.get('JA2103')),
                        is_corp_manufacturing=is_condition_true(li.get('JA2201')),
                        is_corp_agriculture=is_condition_true(li.get('JA2202')),
                        is_corp_it=is_condition_true(li.get('JA2203')),
                        is_corp_other=is_condition_true(li.get('JA2299')),
                        is_disabled=is_condition_true(li.get('JA0328')),
                        is_veteran=is_condition_true(li.get('JA0329')),
                        is_patient=is_condition_true(li.get('JA0330'))
                    )
                    condition.save()
                except SupportServiceList.DoesNotExist:
                    continue

    return Response({'message': '보조금 지원 조건 데이터가 성공적으로 저장/업데이트되었습니다.'})

# 사용자 조건 저장
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_conditions_save(request):
    try:
        # 이미 존재하는 사용자 조건이 있는지 확인
        user_condition = UserConditions.objects.get(user=request.user)
        # 기존 데이터를 업데이트
        serializer = UserConditionsSerializer(user_condition, data=request.data, partial=True)
    except UserConditions.DoesNotExist:
        # 새로운 데이터 생성
        serializer = UserConditionsSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    else:
        # 유효성 검사 실패 시 에러 메시지 반환
        return Response(
            {
                "error": "Invalid data",
                "details": serializer.errors
            }, 
            status=400
        )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def matching_subsidies(request):
    try:
        user_condition = UserConditions.objects.get(user=request.user)
        
        # 기본 쿼리 생성
        matching_query = Q()
        
        # 직업 관련 필터링
        if user_condition.occupation:
            if user_condition.occupation == 'unemployed':
                # 무직인 경우 직업 특화 보조금만 제외
                matching_query &= (
                    ~Q(is_farmer=True) &
                    ~Q(is_fisher=True) &
                    ~Q(is_livestock=True) &
                    ~Q(is_forester=True) &
                    ~Q(service__service_nm__icontains='농업') &
                    ~Q(service__service_nm__icontains='어업') &
                    ~Q(service__service_nm__icontains='수산') &
                    ~Q(service__service_nm__icontains='축산') &
                    ~Q(service__service_nm__icontains='임업') &
                    ~Q(service__service_nm__icontains='해양') &
                    ~Q(service__service_nm__icontains='선원') &
                    ~Q(service__service_nm__icontains='활어') &
                    ~Q(service__service_nm__icontains='산림')
                )
            else:
                # 해당 직업 필드가 True이거나, 일반 보조금 포함
                field_mapping = {
                    'fisher': 'is_fisher',
                    'farmer': 'is_farmer',
                    'livestock': 'is_livestock',
                    'forester': 'is_forester'
                }
                
                if user_condition.occupation in field_mapping:
                    field_name = field_mapping[user_condition.occupation]
                    occupation_query = (
                        Q(**{field_name: True}) |  # 해당 직업 보조금
                        (Q(is_farmer__isnull=True) & 
                         Q(is_fisher__isnull=True) & 
                         Q(is_livestock__isnull=True) & 
                         Q(is_forester__isnull=True))  # 일반 보조금
                    )
                    matching_query &= occupation_query

        # 기존 필터링 로직 유지
        # 성별 조건
        if user_condition.gender == 'male':
            matching_query &= (Q(is_male=True) | Q(is_male__isnull=True))
        else:
            matching_query &= (Q(is_female=True) | Q(is_female__isnull=True))
            
        # 소득 수준 조건
        income_mapping = {
            '0-50': 'income_0_50',
            '51-75': 'income_51_75',
            '76-100': 'income_76_100',
            '101-200': 'income_101_200',
            '200+': 'income_over_200'
        }
        
        if user_condition.income_level in income_mapping:
            field_name = income_mapping[user_condition.income_level]
            matching_query &= (Q(**{field_name: True}) | Q(**{f"{field_name}__isnull": True}))

        # 가구 형태 조건 - 선택하지 않은 조건은 True가 아니어야 함
        household_conditions = {
            'is_multicultural': user_condition.is_multicultural,
            'is_north_defector': user_condition.is_north_defector,
            'is_single_parent': user_condition.is_single_parent,
            'is_single_person': user_condition.is_single_person,
            'is_many_children': user_condition.is_many_children,
            'is_no_house': user_condition.is_no_house,
            'is_new_resident': user_condition.is_new_resident,
        }
        
        for field, value in household_conditions.items():
            if value:
                matching_query &= (Q(**{field: True}) | Q(**{f"{field}__isnull": True}))
            else:
                matching_query &= ~Q(**{field: True})

        # 나머지 조건들도 같은 방식으로 수정
        lifecycle_conditions = {
            'is_expecting': user_condition.is_expecting,
            'is_pregnant': user_condition.is_pregnant,
            'is_birth': user_condition.is_birth,
        }
        
        for field, value in lifecycle_conditions.items():
            if value:
                matching_query &= (Q(**{field: True}) | Q(**{f"{field}__isnull": True}))
            else:
                matching_query &= ~Q(**{field: True})

        # 특수 조건도 같은 방식으로 수정
        special_conditions = {
            'is_disabled': user_condition.is_disabled,
            'is_veteran': user_condition.is_veteran,
            'is_patient': user_condition.is_patient,
        }
        
        for field, value in special_conditions.items():
            if value:
                matching_query &= (Q(**{field: True}) | Q(**{f"{field}__isnull": True}))
            else:
                matching_query &= ~Q(**{field: True})

        # 해당 직업 조건이 True이거나 모든 직업 필드가 null인 경우만 포함
        occupation_mapping = {
            'fisher': ('is_fisher', ['수산', '어업', '어선', '어가', '양식', '선원']),
            'farmer': ('is_farmer', ['농업', '농가', '농지', '농작물']),
            'livestock': ('is_livestock', ['축산', '낙농', '사육']),
            'forester': ('is_forester', ['임업', '산림', '목재'])
        }
        
        if user_condition.occupation in occupation_mapping:
            field_name, keywords = occupation_mapping[user_condition.occupation]
            
            # 직업 관련 보조금 OR 일반 보조금
            occupation_query = (
                Q(**{field_name: True}) |  # 직업 필드가 True인 경우
                Q(**{f"{field_name}__isnull": True})  # 직업 필드가 null인 경우 (일반 보조금)
            )
            
            # 직업 관련 키워드가 포함된 경우도 포함
            for keyword in keywords:
                occupation_query |= Q(service__service_nm__icontains=keyword)
            
            matching_query &= occupation_query

        # 매칭되는 보조금 조건 찾기
        matching_conditions = SupportConditions.objects.filter(matching_query)
        
        # 매칭된 보조금 서비스 정보 가져오기
        matching_services = SupportServiceList.objects.filter(
            service_id__in=matching_conditions.values_list('service_id', flat=True)
        ).distinct()
        
        # 필터링된 결과를 직렬화하여 JSON 형태로 반환
        serializer = SupportServiceListSerializer(matching_services, many=True)
        return Response(serializer.data)
        
    except UserConditions.DoesNotExist:
        return Response(
            {"error": "사용자 조건 정보를 찾을 수 없습니다."}, 
            status=404
        )
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_product_like(request, product_type, product_id):
    user = request.user
    
    try:
        if product_type == 'deposit':
            product = DepositProducts.objects.get(fin_prdt_cd=product_id)
            if user.deposit_products.filter(fin_prdt_cd=product_id).exists():
                user.deposit_products.remove(product)
                return Response({'status': 'unliked'})
            else:
                user.deposit_products.add(product)
                return Response({'status': 'liked'})
        
        elif product_type == 'saving':
            product = SavingProducts.objects.get(fin_prdt_cd=product_id)
            if user.saving_products.filter(fin_prdt_cd=product_id).exists():
                user.saving_products.remove(product)
                return Response({'status': 'unliked'})
            else:
                user.saving_products.add(product)
                return Response({'status': 'liked'})
                
    except (DepositProducts.DoesNotExist, SavingProducts.DoesNotExist):
        return Response({'error': '상품을 찾을 수 없습니다.'}, status=404)
    
@api_view(['get'])
@permission_classes([IsAuthenticated])
def get_ratio(request, answer_id):
    try:
        financial_product = FinancialProduct.objects.get(answer_id=answer_id)
        serializer = SaveInvRatioSerializer(financial_product)
        return Response(serializer.data)
    except FinancialProduct.DoesNotExist:
        return Response({"detail": "Portfolio not found"}, status=404)
    
    