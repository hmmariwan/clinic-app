from django.urls import path,include
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from django.views.i18n import set_language

urlpatterns = [
    # ... your other url patterns ...
    path('i18n/', include('django.conf.urls.i18n')),
    path('set_language/', set_language, name='set_language'), 
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('private_fees/',views.private_fees,name='private_fees'),
    path('nhs_fees/',views.nhs_fees,name='nhs_fees'),
    path('contact/',views.contact,name='contact'),
    path('treatment/general_dentistry/fillings',views.fillings,name='fillings'),
    path('treatment/general_dentistry/dental_hygiene',views.dental_hygiene,name='dental_hygiene'),
    path('treatment/cosmetic_dentistry/',views.cosmetic_dentistry,name='cosmetic_dentistry'),
    path('treatment/specialist_dentistry/',views.specialist_dentistry,name='specialist_dentistry'),
    path('new_patients/',views.new_patients,name='new_patients'),
    path('team/david_terry/',views.david_terry,name='david_terry'),
    path('team/silvia_omer/',views.silvia_omer,name='silvia_omer'),

]


