"""atelier1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

import blog
from blog import views

from blog.views import post_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path("home", views.home2, name="index"),
    path("cars", views.cars, name="cars"),
    path("services", views.services, name="services"),
    path('patient', views.patient_list, name='patient'),
    path('create_patient', views.create_patient, name='create_patient'),
    path('update_patient/<int:pk>', views.update_patient, name='update_patient'),
    path('delete_patient/<int:pk>', views.delete_patient, name='delete_patient')

]
