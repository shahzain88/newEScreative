from django.urls import path
from . import views as home_views

urlpatterns = [
    path('', home_views.home),
    path('kobutsusho/',home_views.kobutsusho)


]
