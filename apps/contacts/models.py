from django.db import models
from apps.base import models as base_models
from apps.secondary import models as secon_models
from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField 
# Create your models here.

class StartMailing(models.Model):
    group = models.ForeignKey(
        secon_models.AddChat,
        on_delete = models.CASCADE,
        related_name = "start_group",
        verbose_name = "Выберите группу в которую хотите отправить рассылку"
    )
    mounth = models.ForeignKey(
        base_models.AddMounthTeach,
        on_delete = models.CASCADE,
        related_name = "start_mounth",
        verbose_name = "Выберите месяц группы"
    )
    devop = models.ForeignKey(
        base_models.AddDevop,
        on_delete = models.CASCADE,
        related_name = "start_devip",
        verbose_name = "Выберите направление группы"
    )
    teacher = models.ForeignKey(
        secon_models.AddTeacher,
        on_delete = models.CASCADE,
        related_name = "start_day",
        verbose_name = "Выберите преподователя"
    )
    admin = models.ForeignKey(
        secon_models.AddAdmin,
        on_delete = models.CASCADE,
        related_name = "start_day",
        verbose_name = "Выберите куратора"
    )
    date = models.DateField(
        verbose_name = "Выберите дату старта"
    )
    hours = models.ForeignKey(
        base_models.AddHours,
        on_delete = models.CASCADE,
        related_name = "start_day",
        verbose_name = "Выберите часовой график"
    )
    day = models.ForeignKey(
        base_models.AddDay,
        on_delete = models.CASCADE,
        related_name = "start_day",
        verbose_name = "Выберите дневной график"
    )

    def __str__(self):
        return f"{self.group} - {self.teacher}"
    
    class Meta:
        verbose_name = "1) Отправить рассылку  старте"
        verbose_name_plural = "1) Отправить рассылку  старте"


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from apps.telegram_bot.views import send_message_to_group  # Импортируем функцию из views.py
        send_message_to_group(self)


class MailingGroup(models.Model):
    group = models.ManyToManyField(
        secon_models.AddChat,
        related_name = "mailing_group",
        verbose_name = "Выберите группу в которую хотите отправить рассылку",
        blank=True
    )
    send_to_all = models.BooleanField(default=False, verbose_name="Отправить всем группам")
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='team_image/',
        verbose_name="Фотография",
        blank = True, null = True
    )

    descriptions = RichTextField(
        verbose_name='Описание 2'
    )


    def __str__(self):
        return f"{self.group} "
    
    class Meta:
        verbose_name = "1) Отправить рассылку  всем"
        verbose_name_plural = "1) Отправить рассылку  всем"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from apps.telegram_bot.views import send_message_with_image
        send_message_with_image(self)