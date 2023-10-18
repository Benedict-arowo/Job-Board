# Generated by Django 4.2.6 on 2023-10-18 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_jobboard', '0008_alter_job_application_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='currency',
            field=models.CharField(blank=True, default='USD', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='employer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='skills_required',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
