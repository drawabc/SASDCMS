from CMSApp import views
from django.conf.urls import url

app_name = 'CMSApp'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^input/$', views.input, name='input'),
    url(r'^manage/$', views.manage_dashboard, name='manage_dashboard')
]