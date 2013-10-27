# coding: utf-8
from django.http import HttpResponse

from schedule.models import *
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

def send_file(request):
    from icalendar import Calendar, Event as Ev
    from datetime import datetime
    import pytz
    import time

    cal = Calendar()
    cal.add('prodid','//Delteps//OurCalendarObjectHackFmi')
    cal.add('version','2.0')
    cal.add('method','publish')

    i = 0
    for ev in Event.objects.all():
        event = Ev()
        event.add('summary',ev.subject.name)
        event.add('dtstart',ev.date_start)
        event.add('dtend', datetime(ev.date_start.year,ev.date_start.month,ev.date_start.day,ev.date_start.hour+ev.duratation,ev.date_start.minute))
        event.add('dtstamp',datetime.now())
        # event.add('rrule','FREQ=WEEKLY;UNTIL='+str(ev.date_end.year)+str(ev.date_end.month)+str(ev.date_end.day)+'T'+str(ev.date_end.hour)+str(ev.date_end.minute)+str(ev.date_end.second))
        # event.add('rrule','FREQ=WEEKLY;UNTIL=20140215T000000Z')
        event['uid']=ev.subject.name+'/'+str(i)
        i = i+1
        cal.add_component(event)

    icalstream = cal.to_ical()
    response = HttpResponse(icalstream, mimetype='text/calendar')
    response['Filename'] = 'filename.ics'
    response['Content-Disposition'] = 'attachment; filename=filename.ics'
    return response

