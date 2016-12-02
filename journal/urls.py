#Journal views

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.journal, name='journal'),
    url(r'json/(?P<jsn>in|out|act|org)/$', views.jsonrequest, name='json'),

    
    url(r'table/(?P<typerec>in|out)/$', views.loadTableTemplate, name='loadtable'),

    url(r'actors/$', views.actors, name='actors'),

    
    
    url(r'delrec/(?P<typerec>in|out)/$', views.delrec, name='del_rec'),
    url(r'edit/(?P<typerec>in|out)/(?P<editpk>[0-9]+)/$', views.edit, name='edit_rec'),

    url(r'addnewin/$', views.addnewin, name='add_new_in'),
    url(r'checknum/(?P<typerec>in|out)/$', views.checknum, name='check_num'),
    
    url(r'appoint/$', views.appoint, name='appoint_act'),
    url(r'markdone/$', views.markdone, name='mark_done'),
]
