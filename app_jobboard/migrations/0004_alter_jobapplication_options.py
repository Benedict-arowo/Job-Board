# Generated by Django 4.2.6 on 2023-10-15 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_jobboard', '0003_alter_jobcategory_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobapplication',
            options={'verbose_name_plural': 'Job Applications'},
        ),
    ]
