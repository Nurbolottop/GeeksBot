# Generated by Django 5.0.1 on 2024-01-23 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_remove_daymailing_days_daymailing_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daymailing',
            name='days',
        ),
        migrations.AddField(
            model_name='daymailing',
            name='days',
            field=models.CharField(blank=True, choices=[('monday', 'Понедельник'), ('tuesday', 'Вторник'), ('wednesday', 'Среда'), ('thursday', 'Четверг'), ('friday', 'Пятница'), ('saturday', 'Суббота'), ('sunday', 'Воскресенье')], max_length=10, verbose_name='Выберите дни недели'),
        ),
    ]
