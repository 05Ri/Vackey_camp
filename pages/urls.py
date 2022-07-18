from django.urls import path
from . import views

urlpatterns = [

    path('', views.mainpage),
    path('main/', views.mainpage),

    path('company/', views.company_intro),
    path('company/greeting/', views.company_greeting),
    path('company/members/', views.company_members),
    path('company/visit/', views.company_visit),

    path('product/', views.product_intro),
    path('mysite/', views.product_all),
    path('product/popular/', views.product_popular),
    path('product/sale/', views.product_sale),

    path('contact/', views.contact_intro),
    path('contact/FAQ/', views.contact_faq),
    path('contact/QnA/', views.contact_qna),
    path('contact/us/', views.contact_us),

]
