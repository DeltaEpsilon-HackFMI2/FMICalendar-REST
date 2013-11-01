from django.contrib import admin
from schedule.models import *


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('room_place', 'floor', 'id')

class HierarchyUnitAdmin(admin.ModelAdmin):
    list_display = ('value', 'type_value', 'id')

class BlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
   
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Place,PlaceAdmin)
admin.site.register(HierarchyUnit,HierarchyUnitAdmin)
admin.site.register(Block,BlockAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Comment,CommentAdmin)
