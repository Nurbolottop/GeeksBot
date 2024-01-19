from django.contrib import admin

################################################################################################################################################################################

from apps.secondary import models 

# Register your models here.

class AddStudentFilterAdmin(admin.ModelAdmin):
    list_filter = ('usrname', 'group' )
    list_display = ('usrname', 'group' )
    search_fields = ('usrname', 'group' )
    fieldsets = (
        ('Основная информация', {
            'fields': ( 'group', 'user_id'),
        }),
        ('Дополнительная информация', {
            'fields': ('name', 'age', 'usrname'),
        }),
    )

################################################################################################################################################################################

class AddTeacherFilterAdmin(admin.ModelAdmin):
    list_filter = ('usrname', 'group' )
    list_display = ('usrname', 'group' )
    search_fields = ('usrname', 'group' )
    fieldsets = (
        ('Основная информация', {
            'fields': ( 'group', 'user_id'),
        }),
        ('Дополнительная информация', {
            'fields': ('name', 'age', 'usrname'),
        }),
    )

################################################################################################################################################################################

class AddAdminFilterAdmin(admin.ModelAdmin):
    list_filter = ('usrname', )
    list_display = ('usrname', )
    search_fields = ('usrname', )
    fieldsets = (
        ('Основная информация', {
            'fields': ('user_id',),
        }),
        ('Дополнительная информация', {
            'fields': ('name', 'age', 'usrname'),
        }),
    )

################################################################################################################################################################################


################################################################################################################################################################################

admin.site.register(models.AddStudent, AddStudentFilterAdmin)
admin.site.register(models.AddAdmin, AddAdminFilterAdmin)
admin.site.register(models.AddTeacher, AddTeacherFilterAdmin)


