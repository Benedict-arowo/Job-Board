# Generated by Django 4.2.6 on 2023-10-15 18:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_jobboard', '0006_jobskill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jobcategory',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jobskill',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
