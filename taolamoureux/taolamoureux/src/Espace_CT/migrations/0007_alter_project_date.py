# Generated by Django 5.0.6 on 2024-06-05 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Espace_CT', '0006_project_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(blank=True, default='None', null=True),
        ),
    ]