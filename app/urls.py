from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name="app"),
    path('sobre', views.sobre, name="sobre"),
    path('produtos', views.produtos, name="produtos"),
    path('salvar-usuario', views.salvarUsuario, name="salvarUsuario"),
    path('login', views.loginUsuario, name="loginUsuario"),
    path('dashboard', views.dashboard, name="dashboard"),
    #path('logout', views.logoutUsuario, name="logoutUsuario")

]