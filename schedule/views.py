# coding: utf-8
from django.http import HttpResponse

from schedule.models import HierarchyUnit
from rest_framework.renderers import JSONRenderer


def menu_map(request):
    """
    Get object representing the filtering interface.
    """
    all_programs = HierarchyUnit.objects.filter(type_value=HierarchyUnit.PROGRAM)
    programs_map = {}
    for program in all_programs:
        programs_map[program.value] = {}
        for year in program.get_all_childs():
            programs_map[program.value][year.value] = []
            for group in year.get_all_childs():
                programs_map[program.value][year.value].append(group.value)

    return HttpResponse(JSONRenderer().render({str('test'): programs_map}))


def by_group_id(request, group_id):
    """
    Get all events connected to some studying group.
    """
    


def by_teacher_id(request, teacher_id):
    """
    Get all events connected to some lecturer.
    """
    pass


def by_room_id(request, room_id):
    """
    Get all events connected to some room.
    """
    pass


def by_block_id(request, block_id):
    """
    Get all the optional courses from some block group.
    """
    pass
