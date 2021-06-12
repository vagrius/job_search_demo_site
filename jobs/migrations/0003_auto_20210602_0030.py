# Generated by Django 3.2.3 on 2021-06-01 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0002_auto_20210602_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.OneToOneField(null=True,
                                       on_delete=django.db.models.deletion.CASCADE,
                                       related_name='companies',
                                       to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_username', models.CharField(max_length=64)),
                ('written_phone', models.CharField(max_length=16)),
                ('written_cover_letter', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='applications',
                                              to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='applications',
                                                 to='jobs.vacancy')),
            ],
        ),
    ]
