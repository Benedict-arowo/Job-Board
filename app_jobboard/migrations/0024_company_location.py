# Generated by Django 4.2.6 on 2023-10-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_jobboard', '0023_alter_company_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.TextField(default='location', max_length=255),
            preserve_default=False,
        ),
    ]