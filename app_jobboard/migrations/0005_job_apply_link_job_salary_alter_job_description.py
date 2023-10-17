# Generated by Django 4.2.6 on 2023-10-15 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_jobboard', '0004_alter_jobapplication_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='apply_link',
            field=models.CharField(default='lol', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(),
        ),
    ]