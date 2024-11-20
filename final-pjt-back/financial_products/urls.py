from django.urls import path, include
from . import views

app_name = 'financial_products'
urlpatterns = [
    path('save_deposit/', views.save_deposit, name='deposit'),  #정기 예금 저장
    path('get_deposit/', views.get_depositproducts), # 정기 예금 조회
    path('save_saving/', views.save_saving, name='saving'),
    path('save_answer/', views.save_answer, name='answer'),
]