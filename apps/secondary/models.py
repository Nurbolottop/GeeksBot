from django.db import models
from apps.telegram_bot.telegram_utils import get_chat_title
from apps.base import models as base_models
from apps.telegram_bot.models import TelegramUser

# Create your models here.
class AddChat(models.Model):
    devop = models.ForeignKey(
        base_models.AddDevop,
        related_name = "give_devop",
        on_delete = models.CASCADE
    )
    mounth = models.ForeignKey(
        base_models.AddMounthTeach,
        related_name = "give_devop",
        on_delete = models.CASCADE,
        blank = True,null = True

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
        verbose_name = "3) Добавить группу"
        verbose_name_plural = "3) Добавить группу"


class AddStudent(models.Model):
    group = models.ForeignKey(
        AddChat,
        related_name = "student_group",
        on_delete = models.CASCADE,
        verbose_name = "Выберите группу"
    )
    user_id = models.CharField(
        max_length = 255,
        verbose_name = "Введите id студента"
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = "Введите ФИО студента"
    )
    age = models.DateField(
        verbose_name = "Дата рождения"
    )
    usrname  = models.CharField(
        max_length = 255,
        verbose_name = "username Студента",
        blank = True,null = True
    )

    def save(self, *args, **kwargs):
        if self.user_id and not self.usrname:
            user = TelegramUser.objects.filter(id_user=self.user_id).first()
            if user:
                self.usrname = user.username
        super(AddStudent, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.group}"
    
    class Meta:
        verbose_name = "1) Добавить студента"
        verbose_name_plural = "1) Добавить студента"

class AddTeacher(models.Model):
    group = models.ForeignKey(
        AddChat,
        related_name = "teacher_group",
        on_delete = models.CASCADE,
        verbose_name = "Выберите группу"
    )
    user_id = models.CharField(
        max_length = 255,
        verbose_name = "Введите id учителя"
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = "Введите ФИО учителя"
    )
    age = models.DateField(
        verbose_name = "Дата рождения"
    )
    usrname  = models.CharField(
        max_length = 255,
        verbose_name = "username учителя",
        blank = True,null = True
    )

    def save(self, *args, **kwargs):
        if self.user_id and not self.usrname:
            user = TelegramUser.objects.filter(id_user=self.user_id).first()
            if user:
                self.usrname = user.username
        super(AddTeacher, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.group}"
    
    class Meta:
        verbose_name = "2) Добавить учителя"
        verbose_name_plural = "2) Добавить учителя"

class AddAdmin(models.Model):
    user_id = models.CharField(
        max_length = 255,
        verbose_name = "Введите id администратора"
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = "Введите ФИО администратора"
    )
    age = models.DateField(
        verbose_name = "Дата рождения"
    )
    usrname  = models.CharField(
        max_length = 255,
        verbose_name = "username администратора",
        blank = True,null = True
    )

    def save(self, *args, **kwargs):
        if self.user_id and not self.usrname:
            user = TelegramUser.objects.filter(id_user=self.user_id).first()
            if user:
                self.usrname = user.username
        super(AddAdmin, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} "
    
    class Meta:
        verbose_name = "3) Добавить администратора"
        verbose_name_plural = "3) Добавить администратора"

