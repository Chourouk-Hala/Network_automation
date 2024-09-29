from django.urls import path 
from . import views


urlpatterns = [
    path('reseaux/home', views.home_page),
    path('reseaux/form1', views.form1_page),
    path('reseaux/form2', views.form2_page),
    path('reseaux/form1/RouterConf', views.RouterConf),
    path('reseaux/form2/SwitchConf', views.SwitchConf) 


]