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
    response_data={}
    all_events = []
    all_subjects = Subject.objects.filter(group=HierarchyUnit.objects.get(id=group_id))
    for sub in all_subjects:
        all_events.append(Event.objects.filter(subject=sub)[0])


    for ev in all_events:
        response_data[ev.name] = {'start': ev.date_start, 'end': ev.date_end, 'teacher':ev.teacher.name}

    return HttpResponse(JSONRenderer().render({str('Begin'): response_data}))


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

def by_student_fn(request, fn):
    """
    Get all the optional courses from some student.
    """
    response_data = {}
    all_events = []
    for ev in Event.objects.all():
        if ev in Student.objects.filter(fac_number=fn)[0].events.all():
            all_events.append(ev)


    for ev in all_events:
        response_data[ev.name] = {'start': ev.date_start, 'end': ev.date_end, 'teacher':ev.teacher.name}

    return HttpResponse(JSONRenderer().render({str('Begin'): response_data}))

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
        event.add('dtend', ev.date_end)
        event.add('dtstamp',datetime.now())        
        event['uid']=ev.subject.name+'/'+str(i)
        i = i+1
        cal.add_component(event)

    icalstream = cal.to_ical()
    response = HttpResponse(icalstream, mimetype='text/calendar')
    response['Filename'] = 'filename.ics'
    response['Content-Disposition'] = 'attachment; filename=filename.ics'
    return response

