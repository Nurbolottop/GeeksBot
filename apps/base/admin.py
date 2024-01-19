from django.contrib import admin
from django.contrib.auth.models import User,Group

################################################################################################################################################################################

from apps.base import models 
from apps.secondary import models as base_models
# Register your models here.

class AddDevopFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

################################################################################################################################################################################

class AddChatFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

################################################################################################################################################################################

class AddMounthTeachFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

################################################################################################################################################################################

class AddDayFilterAdmin(admin.ModelAdmin):
    list_filter = ('day', )
    list_display = ('day', )
    search_fields = ('day', )

################################################################################################################################################################################

class AddHoursFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

################################################################################################################################################################################

################################################################################################################################################################################

admin.site.register(models.AddDevop, AddDevopFilterAdmin)
admin.site.register(models.AddDay, AddDayFilterAdmin)
admin.site.register(models.AddHours, AddHoursFilterAdmin)
admin.site.register(base_models.AddChat, AddChatFilterAdmin)
admin.site.register(models.AddMounthTeach, AddMounthTeachFilterAdmin)



################################################################################################################################################################################

admin.site.unregister(User)
admin.site.unregister(Group)