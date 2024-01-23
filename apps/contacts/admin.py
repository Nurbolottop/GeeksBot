from django.contrib import admin

from apps.contacts import models

# Register your models here.

class StartMailingFilterAdmin(admin.ModelAdmin):
    list_filter = ('group','devop', 'teacher', 'mounth', )
    list_display = ('group','devop', 'teacher', 'mounth', )
    search_fields = ('group','devop', 'teacher', 'mounth', )

################################################################################################################################################################################

class MailingGroupFilterAdmin(admin.ModelAdmin):
    list_filter = ('group',)
    search_fields = ('group',)

#######################################efghng#########################################################################################################################################

class DayAddInline(admin.TabularInline):
    model = models.DayAdd
    extra = 1  

class DayMailingFilterAdmin(admin.ModelAdmin):
    list_display = ('group', 'active', 'lesson_time', 'time')
    search_fields = ('group',)
    inlines = [DayAddInline]
################################################################################################################################################################################

admin.site.register(models.DayMailing, DayMailingFilterAdmin)
admin.site.register(models.MailingGroup, MailingGroupFilterAdmin)
admin.site.register(models.StartMailing, StartMailingFilterAdmin)
