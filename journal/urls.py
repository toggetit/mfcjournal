#Journal views

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.journal, name='journal'),
    url(r'json/(?P<jsn>in|out)/$', views.jsonrequest),

    url(r'addnewin/$', views.addnewin, name='add_new_in'),
    url(r'delrec/(?P<typerec>in|out)$', views.delrec, name='del_rec'),
]
