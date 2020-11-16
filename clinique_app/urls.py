from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('services/<int:id>', views.detail_services, name='detail_services'),
    path('stuff', views.stuff, name='staff'),
    path('staff/<int:id>', views.detail_staff, name='detail_staff'),
    path('promo', views.promo, name='promo'),
    path('promo/i', views.detail_promo, name='detail_promo'),
    path('qa-page', views.qa, name='qa'),
    path('prices', views.price, name='prices'),
    path('contacts', views.contacts, name='contacts'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)