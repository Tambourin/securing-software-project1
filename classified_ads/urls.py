from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginView, name='loginView'),
    path('dologin', views.login, name='login'),
    path('setpassword', views.setPassword, name='setPassword'),
    path('newpassword', views.newPassword, name='newPassword'),
    path('add', views.addView, name='addView')

]