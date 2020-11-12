from django.shortcuts import render


def index(request):
    return render(request, '_index.html')


def about(request):
    return render(request, '_about.html')


def services(request):
    return render(request, '_services.html')


def staff(request):
    return render(request, '_staff.html')


def promo(request):
    return render(request, '_promo.html')


def qa(request):
    return render(request, '_qa.html')

def detail_staff(request):
    return render(request, '_detailstaff.html')