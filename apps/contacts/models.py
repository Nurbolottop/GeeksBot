from django.db import models
from apps.base import models as base_models
from apps.secondary import models as secon_models
from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField 
from django.utils import timezone
import schedule
import threading
import time  # Добавьте этот импорт
from apps.telegram_bot.views import send_message_to_group_day

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
        return f"Рассылка номер: {self.id}"
    
    class Meta:
        verbose_name = "2) Отправить рассылку  всем"
        verbose_name_plural = "2) Отправить рассылку  всем"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from apps.telegram_bot.views import send_message_with_image
        send_message_with_image(self)

class DayMailing(models.Model):
    group = models.ForeignKey(
        secon_models.AddChat,
        related_name="day_group_mailing",
        on_delete=models.CASCADE,
        verbose_name="Выберите группу"
    )
    active = models.BooleanField(
        default=False,
        verbose_name="Включить/Отключить"
    )
    lesson_time = models.TimeField(
        verbose_name="Время урока",
        blank=True, null=True
    )
    time = models.TimeField(
        verbose_name="Выберите время",
        blank=True, null=True
    )

    def __str__(self):
        return f"Рассылка номер: {self.id}"

    class Meta:
        verbose_name = "3) Настроить дневную рассылку"
        verbose_name_plural = "3) Настроить дневную рассылку"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Если рассылка активна, планируем отправку сообщения в указанное время и день
        if self.active:
            for day_add in self.day_mailing.all():
                scheduled_time = timezone.make_aware(timezone.datetime.combine(day_add.days, self.time))
                now = timezone.now()

                # Если время уже прошло, переносим отправку на следующий день
                if now > scheduled_time:
                    scheduled_time += timezone.timedelta(days=1)

                # Вычисляем разницу во времени между текущим моментом и временем отправки
                time_difference = (scheduled_time - now).total_seconds()

                # Запускаем таймер для отправки сообщения по расписанию
                threading.Timer(time_difference, send_message_to_group_day, args=[self]).start()

class DayAdd(models.Model):
    mailing = models.ForeignKey(
        DayMailing,
        related_name="day_mailing",
        on_delete=models.CASCADE,
        verbose_name="Добавьте дни"
    )
    days = models.DateField(
        verbose_name="Выберите день",
        blank=True, null=True
    )