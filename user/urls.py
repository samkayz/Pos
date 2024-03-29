from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('signup', views.register, name='signup'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('update', views.update, name='update'),
]
