from django.contrib.auth import views as auth_views
from django.conf.urls import url
from authentication import views

app_name = 'authentication'
urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(), {'template_name': 'registration/login.html'},name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^manage/$', views.manage_dashboard, name='manage_dashboard'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^delete/(?P<user_pk>\w+)/$', views.delete_account, name='delete'),
    url(r'^reset_pwd/(?P<user_pk>\w+)/$', views.reset_password, name='reset_pwd'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^change_pwd/(?P<user_pk>\w+)/$', views.change_password, name='change_pwd')
]