from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.PositiveIntegerField()


class Speciality(models.Model):
    code = models.CharField(max_length=32, primary_key=True)
    title = models.CharField(max_length=64)
    logo = models.URLField(default='https://place-hold.it/100x60')


class Vacancy(models.Model):
    title = models.CharField(max_length=128)
    speciality = models.ManyToManyField(Speciality, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    published_at = models.DateField()
