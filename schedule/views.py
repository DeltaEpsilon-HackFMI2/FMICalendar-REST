from schedule.models import HierarchyUnit
from rest_framework.renderers import JSONRenderer


def menu_map(request):
    """
    Get object representing the filtering interface.
    """
    all_programs = HierarchyUnit.objects.filter(type_value=HierarchyUnit.PROGRAM)
    programs_map = {HierarchyUnit.TYPES[0][1]:}

    result = {u'Заявка':programs_map}
    for program in all_programs:
        year_set = program.get_all_childs()
        for year in year_set:
            group_set = year.get_all_childs()        












    for program in all_programs:
        years = program.parent
        years_map = {}
        for year in years:
            groups = years.parent
            groups_map = {}
            for group in groups:
                groups_map[group.name] = {}
            years_map[HierarchyUnit[2][1]] = groups_map
        programs_map[HierarchyUnit[1][1]] = years_map
    JSONRenderer().render({HierarchyUnit[0][1]: programs_map})


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
