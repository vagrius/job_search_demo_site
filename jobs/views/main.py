from django.http import HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views import View

from jobs.models import Company, Speciality, Vacancy, Application
from jobs.forms import ApplicationSendForm


class MainView(View):

    def get(self, request, *args, **kwargs):
        search_query = self.request.GET.get('s', None)
        context = {
            'specialities': Speciality.objects.all(),
            'companies': Company.objects.all(),
            'search_query': search_query,
        }
        return render(request, "main/index.html", context=context)


class SearchView(View):

    def get(self, request, *args, **kwargs):
        search_query = self.request.GET.get('s', None)
        vacancies_found = Vacancy.objects.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )
        context = {
            'specialities': Speciality.objects.all(),
            'companies': Company.objects.all(),
            'search_query': search_query,
            'vacancies_found': vacancies_found,
        }
        return render(request, "main/search.html", context=context)


class VacanciesAll(View):

    def get(self, request, *args, **kwargs):
        context = {
            'vacancies': Vacancy.objects.all(),
            'all_vacancies': True,
        }
        return render(request, "main/vacancies.html", context=context)


class VacanciesBySpeciality(View):

    def get(self, request, *args, **kwargs):
        speciality = get_object_or_404(Speciality, code=kwargs['speciality_code'])
        context = {
            'vacancies': speciality.vacancies.all(),
            'speciality': speciality,
            'all_vacancies': False,
        }
        return render(request, "main/vacancies.html", context=context)


class CompanyView(View):

    def get(self, request, *args, **kwargs):
        company = get_object_or_404(Company, id=kwargs['company_id'])
        context = {
            'company': company,
            'vacancies': Vacancy.objects.filter(company_id=company.id),
        }
        return render(request, "main/company.html", context=context)


class VacancyView(View):

    def get(self, request, *args, **kwargs):
        vacancy = get_object_or_404(Vacancy, id=kwargs['vacancy_id'])
        context = {
            'vacancy': vacancy,
            'skills_redefined': vacancy.skills,
            'form': ApplicationSendForm,
        }
        return render(request, "main/vacancy.html", context=context)

    def post(self, request, *args, **kwargs):
        if request.user.id:
            vacancy = get_object_or_404(Vacancy, id=kwargs['vacancy_id'])
            context = {
                'vacancy': vacancy,
                'skills_redefined': vacancy.skills,
            }
            form = ApplicationSendForm(request.POST)
            if form.is_valid():
                application = form.save(commit=False)
                application.vacancy_id = vacancy.id
                application.user_id = request.user.id
                application.save()
                request.session['application_id'] = application.id
                return redirect('application_send', vacancy_id=vacancy.id)
            context['form'] = form
            return render(request, "main/vacancy.html", context=context)
        else:
            return redirect("login")


class ApplicationSendView(View):

    def get(self, request, *args, **kwargs):
        if 'application_id' not in request.session:
            return redirect("vacancies_all")
        else:
            application = get_object_or_404(Application, id=request.session['application_id'])
            vacancy = get_object_or_404(Vacancy, id=kwargs['vacancy_id'])
            if application.vacancy_id == vacancy.id:
                context = {
                    'vacancy': vacancy,
                }
                return render(request, "main/sent.html", context=context)
            else:
                return redirect("vacancies_all")


def custom_handler500(request):

    return HttpResponseServerError('Ошибка 500: ошибка сервера!')
