from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_products(request):
    user = request.user
    data = {
        'deposit_products': [
            {
                'fin_prdt_cd': product.fin_prdt_cd,
                'kor_co_nm': product.kor_co_nm,
                'fin_prdt_nm': product.fin_prdt_nm,
                # 필요한 다른 필드들 추가
            }
            for product in user.deposit_products.all()
        ],
        'saving_products': [
            {
                'fin_prdt_cd': product.fin_prdt_cd,
                'kor_co_nm': product.kor_co_nm,
                'fin_prdt_nm': product.fin_prdt_nm,
                # 필요한 다른 필드들 추가
            }
            for product in user.saving_products.all()
        ]
    }
    return Response(data)
    