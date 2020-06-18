"""passgen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from passgen_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name = 'home'),  #------->Really important to put / after the name of the view ie. home (Here)
    path('password_generator_page/', views.password_generator_page, name = 'password_generator_page'),
    path('generated_password_page', views.generated_password_page, name = 'result_password_page'),#, name= 'password_result'
    path('about/', views.about_page, name = 'about'),
]
