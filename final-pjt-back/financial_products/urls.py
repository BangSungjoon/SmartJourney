from django.urls import path, include
from . import views

app_name = 'financial_products'
urlpatterns = [
    path('save_deposit/', views.save_deposit, name='deposit'),  #정기 예금 저장
    path('save_deposit_savings/', views.save_deposit_savings),  #정기 예금, 적금 저장
    path('get_deposit/', views.get_depositproducts), # 정기 예금 조회(지도)
    path('get_map_deposit/', views.get_map_depositproducts), # 예금 조회(지도)
    path('get_map_savings/', views.get_map_savingsproducts), # 적금 조회(지도)

    path('recommend_deposit/', views.recommend_deposit), # 정기 예금 조회(추천)
    path('recommend_savings/', views.recommend_savings),
    path('recommend_deposit_detail/', views.recommend_deposit_detail),
    path('recommend_savings_detail/', views.recommend_savings_detail),
    path('save_saving/', views.save_saving, name='saving'),
    path('save_answer/', views.save_answer, name='answer'),
    path('save_ratio/<int:answer_id>/', views.save_ratio),
    path('get_ratio/<int:answer_id>/', views.get_ratio),
    # path('my_portfolios/<int:user_id>/', views.my_portfolios), # 내가 작성한 포트폴리오 정보를 찾아오는 요청
    path('my_portfolios/<int:user_id>/', views.get_user_portfolios),
    path('save_change_money/', views.change_money),
    path('exchange/', views.exchange),
    path('portfolio/<int:portfolio_id>/', views.delete_portfolio),
    path('subsidy_list_save/', views.subsidy_list_save),
    path('subsidy_detail_save/', views.subsidy_detail_save),
    path('support_conditions_save/', views.support_conditions_save),
    path('user_conditions_save/', views.user_conditions_save),
    path('matching_subsidies/', views.matching_subsidies, name='matching_subsidies'),
    path('<str:product_type>_products/<str:product_id>/like/', views.toggle_product_like, name='toggle_product_like'),
    path('api/chatbot/', views.chatbot_response, name='chatbot_response'),
]