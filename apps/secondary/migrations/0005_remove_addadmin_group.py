# Generated by Django 5.0.1 on 2024-01-18 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0004_alter_addstudent_options_addadmin_addteacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addadmin',
            name='group',
        ),
    ]