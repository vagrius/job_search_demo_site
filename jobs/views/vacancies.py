from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View

from jobs.models import Company, Vacancy, Application
from jobs.forms import VacancyForm
from jobs.utils import LoginRequiredMixinCustom


class MyVacanciesListView(LoginRequiredMixinCustom, View):

    def get(self, request, *args, **kwargs):
        company = Company.objects.get(owner_id=request.user.id)
        vacancies = Vacancy.objects.filter(company_id=company.id)
        context = {'vacancies': vacancies}
        return render(request, "personal/vacancies_list.html", context=context)


class VacancyCreateView(LoginRequiredMixinCustom, View):

    def get(self, request, *args, **kwargs):
        form = VacancyForm
        context = {
            'form': form,
            'status': 'new',
        }
        return render(request, "personal/vacancy_create.html", context=context)

    def post(self, request, *args, **kwargs):
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.company_id = Company.objects.get(owner_id=request.user.id).id
            vacancy.published_at = str(datetime.now().date())
            vacancy.save()
            request.session['vacancy_status'] = 'created'
            return redirect("vacancy_edit", vacancy_id=vacancy.id)
        context = {
            'form': form,
        }
        return render(request, "personal/vacancy_create.html", context=context)


class VacancyEditView(LoginRequiredMixinCustom, View):

    def get(self, request, *args, **kwargs):
        vacancy = Vacancy.objects.get(id=kwargs['vacancy_id'])
        company = Company.objects.get(id=vacancy.company_id)
        if company.owner_id == request.user.id:
            initial = {
                'title': vacancy.title,
                'speciality': vacancy.speciality,
                'salary_min': vacancy.salary_min,
                'salary_max': vacancy.salary_max,
                'skills': vacancy.skills,
                'description': vacancy.description,
            }
            form = VacancyForm(initial=initial)
            if 'vacancy_status' not in request.session:
                request.session['vacancy_status'] = ''
            context = {
                'vacancy': vacancy,
                'applications': Application.objects.filter(vacancy_id=vacancy.id),
                'form': form,
                'status': request.session['vacancy_status'],
            }
            request.session['vacancy_status'] = ''
            return render(request, "personal/vacancy_create.html", context=context)
        else:
            return redirect("my_vacancies_list")

    def post(self, request, *args, **kwargs):
        vacancy = Vacancy.objects.get(id=kwargs['vacancy_id'])
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            request.session['vacancy_status'] = 'changed'
            return redirect("vacancy_edit", vacancy_id=vacancy.id)
        context = {
            'form': form,
        }
        return render(request, "personal/vacancy_create.html", context=context)
