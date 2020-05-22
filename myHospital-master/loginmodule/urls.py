from django.urls import path
from loginmodule.views import auth_view,register
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
	path('auth', auth_view,name='auth_view_reg'),
	path('register',register,name="loginmodule_register")
]
