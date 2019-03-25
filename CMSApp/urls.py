from CMSApp import views
from django.conf.urls import url

app_name = 'CMSApp'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^input/$', views.input, name='input'),
    url(r'^detail/(?P<report_pk>\w+)/$', views.detail, name='detail')
]