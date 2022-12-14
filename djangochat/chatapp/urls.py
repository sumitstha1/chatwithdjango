from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import (UserApiView)

urlpatterns = [

    # API Urls
    path('api/v1/users/', views.UserApiView.as_view()),

    path('', views.home_page, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]