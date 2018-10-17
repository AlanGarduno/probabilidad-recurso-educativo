from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cuentas'

urlpatterns = [
    url(r'login/$',auth_views.LoginView.as_view(template_name ='cuentas/login.html'), name='login'),
    url(r'logout/$',auth_views.LogoutView.as_view(), name='logout'),
    url(r'singup/$',views.SingUp.as_view(),name='singup'),
]