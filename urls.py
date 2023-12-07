from django.urls import path
from django.urls import re_path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.login, name='login'),
    path('reg', views.reg, name='reg'),
    path('register_user', views.register_user, name='register_user'),
    path('user_login', views.user_login, name='user_login'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('admin', views.admin, name='admin'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('viewusers', views.viewusers, name='viewusers'),
    path('home', views.index, name='index'),
    path('encode', views.encode, name='encode'),
    path('process_encoding_data', views.process_encoding_data, name='process_encoding_data'),
    path('decode', views.decode, name='decode'),
    path('process_decoding_data', views.process_decoding_data, name='process_decoding_data'),
    path('logout_user', views.logout_user, name='logout_user'),
    # re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)),
]