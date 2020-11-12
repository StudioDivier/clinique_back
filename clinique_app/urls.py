from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('staff', views.staff, name='staff'),
    path('promo', views.promo, name='promo'),
    path('qa', views.qa, name='qa'),
    path('detail_staff', views.detail_staff, name='detail_staff'),

]