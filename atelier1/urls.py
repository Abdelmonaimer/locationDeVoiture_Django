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
from django.conf import settings
from django.conf.urls.static import static

import blog
from blog import views

from blog.views import post_list

urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path("home", views.home2, name="index"),
    path("cars", views.cars, name="cars"),
    path("about", views.about, name="about"),
    path("blog", views.blog, name="blog"),
    path("contact", views.contact, name="contact"),
    path("services", views.services, name="services"),
    path('patient', views.patient_list, name='patient'),
    path('create_patient', views.create_patient, name='create_patient'),
    path('update_patient/<int:pk>', views.update_patient, name='update_patient'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('delete_patient/<int:pk>', views.delete_patient, name='delete_patient')
=======
                  path('admin/', admin.site.urls),
                  path('', include("blog.urls")),
                  path("", views.home2, name="index"),
                  path("home", views.home2, name="index"),
                  path("cars", views.cars, name="cars"),
                  path("about", views.about, name="about"),
                  path("blog", views.blog, name="blog"),
                  path("contact", views.contact, name="contact"),
                  path("services", views.services, name="services"),
                  path('cars_dash', views.cars_dash, name='cars_dash'),
                  path('add_car', views.add_car, name='add_car'),
                  path('update_car/<int:pk>', views.update_car, name='update_car'),
                  path('delete_car/<int:pk>', views.delete_car, name='delete_car'),
                  path('employees', views.employees_dash, name='employees_dash'),
                  path('add_employee', views.add_employee, name='add_employee'),
                  path('update_employee/<int:pk>', views.update_employee, name='update_employee'),
                  path('delete_employee/<int:pk>', views.delete_employees, name='delete_employee'),
                  path('patient', views.patient_list, name='patient'),
                  path('create_patient', views.create_patient, name='create_patient'),
                  path('update_patient/<int:pk>', views.update_patient, name='update_patient'),
                  path('delete_patient/<int:pk>', views.delete_patient, name='delete_patient')
>>>>>>> 71b2973f84cd46777a470613ffa46d669004dbc3

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
