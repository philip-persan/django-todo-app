# Generated by Django 4.1 on 2022-11-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_completed',
            field=models.DateTimeField(blank=True, verbose_name='Completed at'),
        ),
    ]
