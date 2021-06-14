from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    logo = models.ImageField(upload_to=settings.MEDIA_COMPANY_IMAGE_DIR)
    description = models.TextField()
    employee_count = models.PositiveIntegerField()
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='companies',
        null=True
    )


class Speciality(models.Model):
    code = models.CharField(max_length=32, primary_key=True)
    title = models.CharField(max_length=64)
    logo = models.ImageField(upload_to=settings.MEDIA_SPECIALITY_IMAGE_DIR)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=128)
    speciality = models.ForeignKey(
        Speciality,
        on_delete=models.CASCADE,
        related_name='vacancies',
        default='backend'
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='vacancies'
    )
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    published_at = models.DateField()


class Application(models.Model):
    written_username = models.CharField(max_length=64)
    written_phone = models.CharField(max_length=16)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='applications'
    )


class ApplicantStatus(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class ApplicantGrade(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Resume(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='resume',
        null=True
    )
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    status = models.ForeignKey(
        ApplicantStatus,
        on_delete=models.CASCADE,
        related_name='resumes',
        default=3
    )
    salary = models.PositiveIntegerField()
    speciality = models.ForeignKey(
        Speciality,
        on_delete=models.CASCADE,
        related_name='resumes',
        default='backend'
    )
    grade = models.ForeignKey(
        ApplicantGrade,
        on_delete=models.CASCADE,
        related_name='resumes',
        default=2
    )
    education = models.TextField()
    experience = models.TextField()
    portfolio = models.CharField(max_length=128)
