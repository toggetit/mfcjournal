#Journal views

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.journal, name='journal'),
    url(r'json/(?P<jsn>in|out)/$', views.jsonrequest),

    url(r'checknum/(?P<typerec>in|out)/$', views.checknum, name='check_num'),
    url(r'addnewin/$', views.addnewin, name='add_new_in'),
    url(r'delrec/(?P<typerec>in|out)/$', views.delrec, name='del_rec'),
    url(r'appoint/$', views.appoint, name='appoint_act'),
    url(r'markdone/$', views.markdone, name='mark_done'),
]
