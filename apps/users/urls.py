from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^new', views.new),
    url(r'^edit/$', views.edit),
    url(r'^show/(?P<name>\d+)/',views.show),
    url(r'^post/', views.post),
    url(r'^comment/$', views.comment),
    url(r'^edit/(?P<idd>\d+)/', views.admin_edit),
    url(r'^editting/$', views.editting),
    url(r'^pwc/$', views.pwc),
    url(r'^off/$', views.off),
    url(r'^description/$', views.desc),
]