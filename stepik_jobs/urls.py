"""stepik_jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from jobs.views import main_view
from jobs.views import vacancies_all_view
from jobs.views import vacancies_by_speciality_view
from jobs.views import company_view
from jobs.views import vacancy_view

urlpatterns = [
    path('', main_view, name='main'),
    path('vacancies/', vacancies_all_view, name='vacancies_all'),
    path('vacancies/cat/<str:speciality_code>/', vacancies_by_speciality_view, name='vacancies_by_speciality'),
    path('companies/<int:company_id>/', company_view, name='company'),
    path('vacancies/<int:vacancy_id>/', vacancy_view, name='vacancy'),
    path('admin/', admin.site.urls),
]
