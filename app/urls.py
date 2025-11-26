from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name="app"),
    path('sobre', views.sobre, name="sobre"),
    path('produtos', views.produtos, name="produtos")

]