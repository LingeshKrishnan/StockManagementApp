from django.conf.urls import url

from .views import *
from .forms import *




urlpatterns = [
    url(r'^$',index,name='index'),

    url(r'^displayNighty$', displayNighty, name='displayNighty'),
    url(r'^displayInskirt$', displayInskirt, name='displayInskirt'),
    url(r'^displayBlouse$', displayBlouse, name='displayBlouse'),
    url(r'^displaySaree$', displaySaree, name='displaySaree'),

    url(r'^addNighty$', addNighty, name='addNighty'),
    url(r'^addInskirt$', addInskirt, name='addInskirt'),
    url(r'^addBlouse$', addBlouse, name='addBlouse'),
    url(r'^addSaree$', addSaree, name='addSaree'),

    url(r'^editNighty/(?P<pk>\d+)$', editNighty, name='editNighty'),
    url(r'^eidtInskirt/(?P<pk>\d+)$', editInskirt, name='editInskirt'),
    url(r'^eidtBlouse/(?P<pk>\d+)$', editBlouse, name='editBlouse'),    
    url(r'^editSaree/(?P<pk>\d+)$', editSaree, name='editSaree'),

    url(r'^deleteNighty/(?P<pk>\d+)$',deleteNighty,name='deleteNighty'),
    url(r'^deleteInskirt/(?P<pk>\d+)$',deleteInskirt,name='deleteInskirt'),
    url(r'^deleteBlouse/(?P<pk>\d+)$',deleteBlouse,name='deleteBlouse'),
    url(r'^deleteSaree/(?P<pk>\d+)$',deleteSaree,name='deleteSaree'),
]