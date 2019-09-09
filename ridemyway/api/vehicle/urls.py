from django.urls import path

from . import views


app_name = 'vehicle'

urlpatterns = [
    path('vehicles/', views.VehicleView.as_view(), name='create_list_vehicles'),
]
