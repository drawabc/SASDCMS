from django.contrib.auth import views as auth_views
from django.conf.urls import url
from authentication import views

app_name = 'authentication'
urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'},name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^manage/$', views.manage_dashboard, name='manage_dashboard'),
    url(r'^signup/$', views.signup, name='signup')
]