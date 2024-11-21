from django.urls import path, include
from . import views

app_name = 'financial_products'
urlpatterns = [
    path('save_deposit/', views.save_deposit, name='deposit'),
    path('save_saving/', views.save_saving, name='saving'),
    path('save_answer/', views.save_answer, name='answer'),
    path('save_ratio/<int:answer_id>/', views.save_ratio),
    path('my_portfolios/<int:user_id>/', views.my_portfolios), # 내가 작성한 포트폴리오 정보를 찾아오는 요청
    path('save_change_money/', views.change_money),
    path('exchange/', views.exchange),
]