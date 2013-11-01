from django.contrib import admin
from schedule.models import *


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

admin.site.register(Place)
admin.site.register(HierarchyUnit)
admin.site.register(Block)
admin.site.register(Subject)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Teacher)
admin.site.register(Event)
admin.site.register(Student)
admin.site.register(Comment)
