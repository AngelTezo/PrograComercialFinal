from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.menu_list, name='menu_list'),
    url(r'^restaurante/menu/agregar$', views.menu_nuevo, name='menu_nuevo'),

    ] 