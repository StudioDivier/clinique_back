from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models



def index(request):
    # if request.method == 'POST':
    #     PricesForm = forms.PricesForm(request.POST)
    ddd = {'asf': 'sdf'}
    sd = not not ddd
    return render(request, '_index.html')


def about(request):
    return render(request, '_about.html')


def services(request):
    return render(request, '_services.html')


def staff(request):
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

    subdirection = models.SubDirectionsStaff.objects.get(staff=staff.full_name)
    subdirection_list_pre = models.SubDirectionStaffItems.objects.filter(subdir_id=subdirection.id)

    items = {}

    for i in range(len(subdirection_list_pre)):
        subdir_obj = models.Subdirections.objects.get(name_subdirection=subdirection_list_pre[i].subdirection)
        dir_items = models.ItemsSubDirection.objects.filter(subdirection_id_id=subdir_obj.id)
        for j in range(len(dir_items)):
            data= []
            data.append(dir_items[j].item)
        items['item'] = data
    print(items)
    return render(request, '_detailstaff.html', {
        'staff': staff, 'information_text': information_text, 'information_li': information_li,
        'education_li': education_li, 'items': items
    }
                  )


def promo(request):
    return render(request, '_promo.html')


def qa(request):
    return render(request, '_qa.html')