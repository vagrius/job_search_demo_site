from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from jobs.models import Company, Speciality, Vacancy


def main_view(request):

    context = {
        'specialities': Speciality.objects.all(),
        'companies': Company.objects.all()
    }

    return render(request, "index.html", context=context)


def vacancies_all_view(request):

    context = {
        'vacancies': Vacancy.objects.all(),
        'all_vacancies': True,
    }

    return render(request, "vacancies.html", context=context)


def vacancies_by_speciality_view(request, speciality_code):

    speciality = get_object_or_404(Speciality, code=speciality_code)

    context = {
        'vacancies': speciality.vacancies.all(),
        'speciality': speciality,
        'all_vacancies': False,
    }

    return render(request, "vacancies.html", context=context)


def company_view(request, company_id):

    company = get_object_or_404(Company, id=company_id)

    context = {
        'company': company,
        'vacancies': Vacancy.objects.filter(company_id=company_id),
    }

    return render(request, "company.html", context=context)


def vacancy_view(request, vacancy_id):

    vacancy = get_object_or_404(Vacancy, id=vacancy_id)

    context = {
        'vacancy': vacancy,
        'skills_redefined': vacancy.skills.replace(', ', ' • '),
    }

    return render(request, "vacancy.html", context=context)


def custom_handler500(request):
    return HttpResponseServerError('Ошибка 500: ошибка сервера!')
