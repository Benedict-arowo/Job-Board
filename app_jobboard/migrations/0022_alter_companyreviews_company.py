# Generated by Django 4.2.6 on 2023-10-24 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_jobboard', '0021_companyreviews_company_alter_companyreviews_reviewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyreviews',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_jobboard.company'),
        ),
    ]
