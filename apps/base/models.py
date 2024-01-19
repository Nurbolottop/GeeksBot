from django.db import models
from apps.telegram_bot.telegram_utils import get_chat_title

# Create your models here.
class AddDevop(models.Model):
    title  = models.CharField(
        max_length = 255,
        verbose_name = "Введите название направления"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "1) Добавить направление"
        verbose_name_plural = "1) Добавить направление"

class AddMounthTeach(models.Model):
    title  = models.CharField(
        max_length = 255,
        verbose_name = "Введите название месяца"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "2) Добавить месяц"
        verbose_name_plural = "2) Добавить месяц"

class AddDay(models.Model):
    day = models.CharField(
        max_length = 255,
        verbose_name = "Введите график дней"
    )
    def __str__(self):
        return self.day
    
    class Meta:
        verbose_name = "3) Добавить график дней"
        verbose_name_plural = "3) Добавить график дней"

class AddHours(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Введите график часов"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "4) Добавить график часов"
        verbose_name_plural = "4) Добавить график часов"