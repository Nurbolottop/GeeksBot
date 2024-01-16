from django.db import models
from apps.telegram_bot.views import get_chat_title
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

class AddChat(models.Model):
    devop = models.ForeignKey(
        AddDevop,
        related_name = "give_devop",
        on_delete = models.CASCADE
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название чата/группы",
        
        blank = True,null = True
    )
    chat_id = models.CharField(
        max_length = 255,
        verbose_name = "Id чата"
    )

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.chat_id and not self.title:
            self.title = get_chat_title(self.chat_id)
        super(AddChat, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "2) Добавить группу"
        verbose_name_plural = "2) Добавить группу"