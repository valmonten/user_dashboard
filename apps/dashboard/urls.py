from django.conf.urls import url
from . import views

urlpatterns=[

    url(r'^$', views.dash),
    url(r'^admin/$', views.admin),
    
]