from data import jobs, companies, specialties
from jobs.models import Company, Speciality, Vacancy

import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'stepik_jobs.settings'
django.setup()


if __name__ == '__main__':

    for company in companies:
        db_company = Company(id=company['id'],
                             name=company['title'],
                             location=company['location'],
                             logo='https://place-hold.it/100x60',
                             description=company['description'],
                             employee_count=company['employee_count'])
        db_company.save()

    for speciality in specialties:
        db_speciality = Speciality(code=speciality['code'],
                                   title=speciality['title'],
                                   logo='https://place-hold.it/100x60')
        db_speciality.save()

    for job in jobs:
        db_vacancy = Vacancy(id=job['id'],
                             title=job['title'],
                             company=Company.objects.get(id=int(job['company'])),
                             skills=job['skills'],
                             description=job['description'],
                             salary_min=job['salary_from'],
                             salary_max=job['salary_to'],
                             published_at=job['posted'])
        db_vacancy.save()
        db_vacancy.speciality.add(Speciality.objects.get(code__iexact=job['specialty']))
        db_vacancy.save()
