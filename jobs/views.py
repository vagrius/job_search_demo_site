from django.http import HttpResponseNotFound, HttpResponseServerError
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

    if not Speciality.objects.filter(code=speciality_code).first():
        return HttpResponseNotFound(f"Специализации с кодом '{speciality_code}' не найдено!")

    speciality = Speciality.objects.filter(code=speciality_code).first()

    context = {
        'vacancies': speciality.vacancies.all(),
        'speciality': speciality,
        'all_vacancies': False,
    }

    return render(request, "vacancies.html", context=context)


def company_view(request, company_id):

    if not Company.objects.filter(id=company_id).first():
        return HttpResponseNotFound(f"Компании с id='{company_id}' не найдено!")

    context = {
        'company': Company.objects.filter(id=company_id).first(),
        'vacancies': Vacancy.objects.filter(company_id=company_id),
    }

    return render(request, "company.html", context=context)


def vacancy_view(request, vacancy_id):

    if not Vacancy.objects.filter(id=vacancy_id).first():
        return HttpResponseNotFound(f"Вакансии с id='{vacancy_id}' не найдено!")

    vacancy = Vacancy.objects.filter(id=vacancy_id).first()

    context = {
        'vacancy': vacancy,
        'skills_redefined': vacancy.skills.replace(', ', ' • '),
    }

    return render(request, "vacancy.html", context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ошибка 404: страница не найдена!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка 500: ошибка сервера!')
