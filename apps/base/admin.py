from django.contrib import admin
from django.contrib.auth.models import User,Group

################################################################################################################################################################################

from apps.base import models 

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


################################################################################################################################################################################

admin.site.register(models.AddDevop, AddDevopFilterAdmin)
admin.site.register(models.AddChat, AddChatFilterAdmin)


################################################################################################################################################################################

admin.site.unregister(User)
admin.site.unregister(Group)