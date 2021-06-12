# Generated by Django 3.2.3 on 2021-06-08 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0005_auto_20210607_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicantStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('salary', models.PositiveIntegerField()),
                ('education', models.TextField()),
                ('experience', models.TextField()),
                ('portfolio', models.CharField(max_length=128)),
                ('grade', models.ForeignKey(default=2,
                                            on_delete=django.db.models.deletion.CASCADE,
                                            related_name='resumes',
                                            to='jobs.applicantgrade')),
                ('speciality', models.ForeignKey(default='backend',
                                                 on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='resumes',
                                                 to='jobs.speciality')),
                ('status', models.ForeignKey(default=3,
                                             on_delete=django.db.models.deletion.CASCADE,
                                             related_name='resumes',
                                             to='jobs.applicantstatus')),
                ('user', models.OneToOneField(null=True,
                                              on_delete=django.db.models.deletion.CASCADE,
                                              related_name='resume',
                                              to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]