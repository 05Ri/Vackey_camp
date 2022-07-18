from django.shortcuts import render


# 메인 페이지
def mainpage(request):
    return render(request, 'pages/mainpage.html')


# 회사 소개 관련
def company_intro(request):
    return render(request, 'pages/company/company_intro.html')


def company_greeting(request):
    return render(request, 'pages/company/company_greeting.html')


def company_members(request):
    return render(request, 'pages/company/company_members.html')


def company_visit(request):
    return render(request, 'pages/company/company_visit.html')


# 상품 소개 관련
def product_intro(request):
    return render(request, 'pages/product/product_intro.html')


def product_all(request):
    return render(request, 'mysite/content_list.html')


def product_popular(request):
    return render(request, 'pages/product/product_popular.html')


def product_sale(request):
    return render(request, 'pages/product/product_sale.html')


# 문의 관련
def contact_intro(request):
    return render(request, 'pages/contact/contact_intro.html')


def contact_faq(request):
    return render(request, 'pages/contact/contact_faq.html')


def contact_qna(request):
    return render(request, 'pages/contact/contact_qna.html')


def contact_us(request):
    return render(request, 'pages/contact/contact_us.html')

