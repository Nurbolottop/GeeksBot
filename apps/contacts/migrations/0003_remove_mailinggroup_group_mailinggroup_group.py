# Generated by Django 5.0.1 on 2024-01-18 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_mailinggroup'),
        ('secondary', '0008_addchat_alter_addstudent_group_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailinggroup',
            name='group',
        ),
        migrations.AddField(
            model_name='mailinggroup',
            name='group',
            field=models.ManyToManyField(related_name='mailing_group', to='secondary.addchat', verbose_name='Выберите группу в которую хотите отправить рассылку'),
        ),
    ]
