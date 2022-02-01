from django.urls import path

from . import views

# Nome do arquivo na url do Browser

app_name = 'manage_tpm'
urlpatterns = [
    path('', views.index, name='index'),
]