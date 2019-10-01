"""ridemyway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.documentation import include_docs_urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/auth/', include('ridemyway.api.authentication.urls')),
    path('api/v1/', include_docs_urls(title='Ride My Way API',
                                           description="Ride-My-Way is an application built to solve several problems within the"
                                           "transportation sector in the economy. This application will involve drivers"
                                           " creating rides with the desired destination and riders being able to request"
                                           " for a ride and it can be shared by different people. With the current system."
                                           "it's very hard to get available drivers in remote areas. With this challenge,"
                                           " both riders and drivers complain about the system.")),
    path('api/v1/', include('ridemyway.api.vehicle.urls')),
]
