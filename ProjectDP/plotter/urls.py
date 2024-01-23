from django.urls import path

from . import views

app_name = 'plotter'
urlpatterns = [
    path('', views.plotter, name='plotter'),
]