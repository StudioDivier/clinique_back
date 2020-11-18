from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

from django.template import RequestContext
from . import models
from . import forms
from .services import database_form
import requests
import json


def handler404(request, exception):
    return render(request, '404.html', status=404)


def index(request):
    if request.method == 'POST':

        form_up = forms.UpForm(request.POST)
        form_price = forms.PricesForm(request.POST)

        if 'exampleModalCenter' in request.POST:
            if form_up.is_valid():
                data = form_up.cleaned_data
                smth = models.Appointment(name=data['name'], phone=data['phone'], email=data['email'],
                                          date=data['date'], service=data['service'])
                smth.save()
            return HttpResponseRedirect('/')

        if 'price_form' in request.POST:
            if form_price.is_valid():
                data = form_price.cleaned_data
                smth = models.GetPrice(name=data['name'], phone=data['phone'],
                                       email=data['email'])
                smth.save()
            return HttpResponseRedirect('/')

    else:
        form_up = forms.UpForm(request.POST)
        form_price = forms.PricesForm(request.POST)
        promo_list = models.Promo.objects.all().order_by('id')
        staff_list = models.Personals.objects.all().order_by('id')
        service_detail_list = models.ServiceDetail.objects.all().order_by('id')
        try:
            get_token = models.TokenInst.objects.filter().last()
            token = get_token.token
        except:
            token = 'IGQVJVcjNxVlZACc2hpaG5FcGxvdW0xbER2UWZAxN2x6azhjdUczRFRfcVRzRmRsQzBzaU83WlRHcUdwZATRZAVVFmaW5kdk5vcnIzWEFBUXJCZAFdLNGNwWWNxN255SkNUajBFX2xXQTRyWHRfZAFFpUGtNUgZDZD'

        link_token = 'https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token={}'.format(token)
        response = requests.get(link_token).json()
        access_token = response['access_token']

        if token != access_token:
            models.TokenInst.objects.filter(token=token).update(token=access_token)

        link_data = 'https://graph.instagram.com/me/media?fields=media_url,permalink&access_token={}'.format(access_token)
        insta_data = requests.get(link_data).json()
        insta_media = insta_data['data'][:8]

        return render(request, '_index.html', {'form_up': form_up, 'form_price': form_price,
                                               'promo_list': promo_list, 'staff_list': staff_list,
                                               'service_detail_list': service_detail_list, 'insta_media': insta_media})


def about(request):
    if request.method == 'POST':

        form_price = forms.PricesForm(request.POST)
        form_up = forms.UpForm(request.POST)

        if 'exampleModalCenter' in request.POST:
            if form_up.is_valid():
                data = form_up.cleaned_data
                smth = models.Appointment(name=data['name'], phone=data['phone'], email=data['email'],
                                          date=data['date'], service=data['service'])
                smth.save()
            return HttpResponseRedirect('/about')

        if 'price_form' in request.POST:
            if form_price.is_valid():
                data = form_price.cleaned_data
                smth = models.GetPrice(name=data['name'], phone=data['phone'],
                                       email=data['email'])
                smth.save()
            return HttpResponseRedirect('/about')

    else:
        form_price = forms.PricesForm(request.POST)
        form_up = forms.UpForm(request.POST)

        return render(request, '_about.html', {'form_price': form_price, 'form_up': form_up})


def services(request):
    if request.method == 'POST':

        form_price = forms.PricesForm(request.POST)
        form_up = forms.UpForm(request.POST)

        if 'exampleModalCenter' in request.POST:
            if form_up.is_valid():
                data = form_up.cleaned_data
                smth = models.Appointment(name=data['name'], phone=data['phone'], email=data['email'],
                                          date=data['date'], service=data['service'])
                smth.save()
            return HttpResponseRedirect('/services')

        if 'price_form' in request.POST:
            if form_price.is_valid():
                data = form_price.cleaned_data
                smth = models.GetPrice(name=data['name'], phone=data['phone'],
                                       email=data['email'])
                smth.save()
            return HttpResponseRedirect('/services')

    else:
        form_price = forms.PricesForm(request.POST)
        form_up = forms.UpForm(request.POST)
        service_list = models.ServicesList.objects.all()
        service_detail_list = models.ServiceDetail.objects.all()

        return render(request, '_services.html', {'service_list': service_list,
                                                  'service_detail_list': service_detail_list,
                                                  'form_price': form_price, 'form_up': form_up})


def detail_services(request, id):
    if request.method == 'POST':
        form_up = forms.UpForm(request.POST)
        form_price = forms.PricesForm(request.POST)

        if 'exampleModalCenter' in request.POST:
            if form_up.is_valid():
                data = form_up.cleaned_data
                smth = models.Appointment(name=data['name'], phone=data['phone'], email=data['email'],
                                          date=data['date'], service=data['service'])
                smth.save()
            return HttpResponseRedirect('/services')

        if 'price_form' in request.POST:
            if form_price.is_valid():
                data = form_price.cleaned_data
                smth = models.GetPrice(name=data['name'], phone=data['phone'],
                                       email=data['email'])
                smth.save()
            return HttpResponseRedirect('/services')

    else:
        form_up = forms.UpForm(request.POST)
        form_price = forms.PricesForm(request.POST)

        service = get_object_or_404(models.ServiceDetail, id=id)
        service_obj = models.ServicesList.objects.get(id=service.service_id)
        # service_detail_list = models.ServiceDetail.objects.all()
        session_prices = models.SessionPrices.objects.filter(service_id=service.id)


        return render(request, '_detailservices.html', {'service': service, 'service_obj': service_obj,
                                                        'session_prices': session_prices, 'form_up': form_up,
                                                        'form_price': form_price})


def price(request):
    if request.method == 'POST':
        form_up = forms.UpForm(request.POST)
        form_price = forms.PricesForm(request.POST)

        if 'exampleModalCenter' in request.POST:
            if form_up.is_valid():
                data = form_up.cleaned_data
                smth = models.Appointment(name=data['name'], phone=data['phone'], email=data['email'],
                                          date=data['date'], service=data['service'])
                smth.save()
            return HttpResponseRedirect('/services')

        if 'price_form' in request.POST:
            if form_price.is_valid():
                data = form_price.cleaned_data
                smth = models.GetPrice(name=data['name'], phone=data['phone'],
                                       email=data['email'])
                smth.save()
            return HttpResponseRedirect('/prices')

    else:
        form_up = forms.UpForm(request.POST)
        form_price = forms.PricesForm(request.POST)
        return render(request, '_prices.html', {'form_price': form_price, 'form_up': form_up})


def promo(request):
    if request.method == 'POST':
        form_up = forms.UpForm(request.POST)
        form_price = forms.PricesForm(request.POST)

        if 'exampleModalCenter' in request.POST:
            if form_up.is_valid():
                data = form_up.cleaned_data
                smth = models.Appointment(name=data['name'], phone=data['phone'], email=data['email'],
                                          date=data['date'], service=data['service'])
                smth.save()
            return HttpResponseRedirect('/promo')

        if 'price_form' in request.POST:
            if form_price.is_valid():
                data = form_price.cleaned_data
                smth = models.GetPrice(name=data['name'], phone=data['phone'],
                                       email=data['email'])
                smth.save()
            return HttpResponseRedirect('/promo')

    else:
        form_up = forms.UpForm(request.POST)
        form_price = forms.PricesForm(request.POST)
        promo_list = models.Promo.objects.all().order_by('id')

        return render(request, '_promo.html', {'promo_list': promo_list, 'form_price': form_price,
                                               'form_up': form_up})


def detail_promo(request, id):
    if request.method == 'POST':
        form_up = forms.UpForm(request.POST)

        if 'exampleModalCenter' in request.POST:
            if form_up.is_valid():
                data = form_up.cleaned_data
                smth = models.Appointment(name=data['name'], phone=data['phone'], email=data['email'],
                                          date=data['date'], service=data['service'])
                smth.save()
            return HttpResponseRedirect('/promo')

    else:
        form_up = forms.UpForm(request.POST)

        promo = get_object_or_404(models.Promo, id=id)
        promo_result_points = models.PromoResultPoints.objects.filter(post_result=id)
        promo_prices = models.PromoPrices.objects.filter(service_id=id)

        return render(request, '_detailpromo.html', {'promo': promo, 'promo_result_points': promo_result_points,
                                                     'promo_prices': promo_prices, 'form_up': form_up})


def staff(request):
    if request.method == 'POST':

        form_price = forms.PricesForm(request.POST)
        form_up = forms.UpForm(request.POST)

        if 'exampleModalCenter' in request.POST:
            if form_up.is_valid():
                data = form_up.cleaned_data
                smth = models.Appointment(name=data['name'], phone=data['phone'], email=data['email'],
                                          date=data['date'], service=data['service'])
                smth.save()
            return HttpResponseRedirect('/staff')

        if 'price_form' in request.POST:
            if form_price.is_valid():
                data = form_price.cleaned_data
                smth = models.GetPrice(name=data['name'], phone=data['phone'],
                                       email=data['email'])
                smth.save()
            return HttpResponseRedirect('/staff')

    else:
        form_price = forms.PricesForm(request.POST)
        form_up = forms.UpForm(request.POST)
        staff_list = models.Personals.objects.all()

        return render(request, '_staff.html', {'staff_list': staff_list, 'form_price': form_price,
                                               'form_up': form_up})


def detail_staff(request, id):
    """

    :param request:
    :param id:
    :return:
    """
    if request.method == 'POST':
        form_up = forms.UpForm(request.POST)

        if 'exampleModalCenter' in request.POST:
            if form_up.is_valid():
                data = form_up.cleaned_data
                smth = models.Appointment(name=data['name'], phone=data['phone'], email=data['email'],
                                          date=data['date'], service=data['service'])
                smth.save()
            return HttpResponseRedirect('/staff')

    else:
        form_up = forms.UpForm(request.POST)

        staff = get_object_or_404(models.Personals, id=id)

        information_text = models.Informations.objects.get(staff=staff.full_name)
        information_li = models.InfoDirections.objects.filter(info_id_id=information_text.id)

        education_text = models.Educations.objects.get(staff=staff.full_name)
        education_li = models.EducationItems.objects.filter(ed_id_id=education_text.id)

        direction = models.DirectionsStaff.objects.get(staff=staff.full_name)
        direction_list = models.DirectionStaffItems.objects.filter(dir_id=direction.id)

        subdirection_all = models.Subdirections.objects.all()
        items_sub = models.ItemsSubDirection.objects.all()

        return render(request, '_detailstaff.html', {
            'staff': staff, 'information_text': information_text, 'information_li': information_li,
            'education_li': education_li, 'direction_list': direction_list, 'subdirection_all': subdirection_all,
            'items_sub': items_sub, 'form_up':form_up
        }
                      )


def qa(request):
    if request.method == 'POST':

        form_price = forms.PricesForm(request.POST)
        form_up = forms.UpForm(request.POST)

        if 'exampleModalCenter' in request.POST:
            if form_up.is_valid():
                data = form_up.cleaned_data
                smth = models.Appointment(name=data['name'], phone=data['phone'], email=data['email'],
                                          date=data['date'], service=data['service'])
                smth.save()
            return HttpResponseRedirect('/qa-page')

        if 'price_form' in request.POST:
            if form_price.is_valid():
                data = form_price.cleaned_data
                smth = models.GetPrice(name=data['name'], phone=data['phone'],
                                       email=data['email'])
                smth.save()
            return HttpResponseRedirect('/qa-page')

    else:
        form_price = forms.PricesForm(request.POST)
        form_up = forms.UpForm(request.POST)
        return render(request, '_qa.html', {'form_price': form_price, 'form_up': form_up})


def contacts(request):
    if request.method == 'POST':

        form_price = forms.PricesForm(request.POST)
        form_up = forms.UpForm(request.POST)

        if 'exampleModalCenter' in request.POST:
            if form_up.is_valid():
                data = form_up.cleaned_data
                smth = models.Appointment(name=data['name'], phone=data['phone'], email=data['email'],
                                          date=data['date'], service=data['service'])
                smth.save()
            return HttpResponseRedirect('/qa-page')

        if 'price_form' in request.POST:
            if form_price.is_valid():
                data = form_price.cleaned_data
                smth = models.GetPrice(name=data['name'], phone=data['phone'],
                                       email=data['email'])
                smth.save()
            return HttpResponseRedirect('/contacts')

    else:
        form_price = forms.PricesForm(request.POST)
        form_up = forms.UpForm(request.POST)

        return render(request, '_contacts.html', {'form_price': form_price, 'form_up':form_up})


