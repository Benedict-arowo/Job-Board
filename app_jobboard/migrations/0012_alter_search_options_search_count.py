# Generated by Django 4.2.6 on 2023-10-19 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_jobboard', '0011_alter_job_currency_search'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='search',
            options={'verbose_name_plural': 'Searches'},
        ),
        migrations.AddField(
            model_name='search',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
