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
from django.conf import settings
from django.conf.urls.static import static

from jobs.views.main import MainView
from jobs.views.main import SearchView
from jobs.views.main import VacanciesAll
from jobs.views.main import VacanciesBySpeciality
from jobs.views.main import CompanyView
from jobs.views.main import VacancyView
from jobs.views.main import ApplicationSendView

from jobs.views.company import CompanyStartView
from jobs.views.company import CompanyCreateView
from jobs.views.company import CompanyMyView

from jobs.views.vacancies import MyVacanciesListView
from jobs.views.vacancies import VacancyCreateView
from jobs.views.vacancies import VacancyEditView

from jobs.views.resume import ResumeStartView
from jobs.views.resume import ResumeCreateView
from jobs.views.resume import ResumeMyView

from accounts.views import RegisterUser
from accounts.views import LoginUser
from accounts.views import logout_user

urlpatterns = [
    # основная часть сайта
    path('', MainView.as_view(), name='main'),
    path('search', SearchView.as_view(), name='search'),
    path('vacancies/', VacanciesAll.as_view(), name='vacancies_all'),
    path('vacancies/cat/<str:speciality_code>/', VacanciesBySpeciality.as_view(), name='vacancies_by_speciality'),
    path('companies/<int:company_id>/', CompanyView.as_view(), name='company'),
    path('vacancies/<int:vacancy_id>/', VacancyView.as_view(), name='vacancy'),
    path('vacancies/<int:vacancy_id>/send/', ApplicationSendView.as_view(), name='application_send'),
    path('admin/', admin.site.urls),
    # личный кабинет - моя компания
    path('mycompany/letsstart/', CompanyStartView.as_view(), name='company_start'),
    path('mycompany/create/', CompanyCreateView.as_view(), name='company_create'),
    path('mycompany/', CompanyMyView.as_view(), name='company_my'),
    # личный кабинет - вакансии
    path('mycompany/vacancies', MyVacanciesListView.as_view(), name='my_vacancies_list'),
    path('mycompany/vacancies/create/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('mycompany/vacancies/<int:vacancy_id>/', VacancyEditView.as_view(), name='vacancy_edit'),
    # личный кабинет - резюме
    path('myresume/letsstart/', ResumeStartView.as_view(), name='resume_start'),
    path('myresume/create/', ResumeCreateView.as_view(), name='resume_create'),
    path('myresume/', ResumeMyView.as_view(), name='resume_my'),
    # пользователи
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
