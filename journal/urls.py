#Journal views

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.journal, name='journal'),
    url(r'json/(?P<jsn>in|out)/$', views.json),

    url(r'addnewin/$', views.addnewin),
]
