from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from . import models
from . import forms
from .services import database_form


def index(request):
    if request.method == 'POST':

        form_up = forms.UpForm(request.POST)
        form_price = forms.PricesForm(request.POST)

        if 'exampleModalCenter' in request.POST:
            if form_up.is_valid():
                data = form_up.cleaned_data
                database_form.upformForward(name=data['name'], phone=data['phone'], email=data['email'],
                                            date=data['date'], service=data['service'])

                return HttpResponseRedirect('/')

        if 'price_form' in request.POST:
            if form_price.is_valid():
                data = form_price.cleaned_data
                smth = database_form.priceformForward(name=data['name'], phone=data['phone'], email=data['email'])

                return HttpResponseRedirect('/')

    else:
        form_up = forms.UpForm(request.POST)
        form_price = forms.PricesForm(request.POST)

        return render(request, '_index.html', {'form_up': form_up, 'form_price': form_price})


def about(request):
    return render(request, '_about.html')


def services(request):
    service_list = models.ServicesList.objects.all()
    service_detail_list = models.ServiceDetail.objects.all()

    return render(request, '_services.html', {'service_list': service_list,
                                                    'service_detail_list': service_detail_list,})


def detail_services(request, id):

    service = get_object_or_404(models.ServiceDetail, id=id)

    service_obj = models.ServicesList.objects.get(id=service.service_id)
    # service_detail_list = models.ServiceDetail.objects.all()
    session_prices = models.SessionPrices.objects.filter(service_id=service.id)


    return render(request, '_detailservices.html', {'service': service, 'service_obj': service_obj,
                                                    'session_prices': session_prices})


def price(request):
    return render(request, '_prices.html')


def promo(request):
    return render(request, '_promo.html')


def detail_promo(request):
    return render(request, '_detailpromo.html')

def stuff(request):
    staff_list = models.Personals.objects.all()

    return render(request, '_staff.html', {'staff_list': staff_list})


def detail_staff(request, id):
    """

    :param request:
    :param id:
    :return:
    """
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
        'items_sub': items_sub
    }
                  )


def qa(request):
    return render(request, '_qa.html')


def contacts(request):
    return render(request, '_contacts.html')


