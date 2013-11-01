from schedule.models import *
import json

json_data = open('C:\\Users\\simeon.COMSOFTL\\Desktop\\HackFMI-backend\\FMICalendar-REST\\FMI-Data-master\\teachers.json','rb')

data = json.load(json_data)

departmentsMap={u'���': 1, u'��':2, u'����':3, u'����':4, u'��':5, u'��':6, u'��':7, u'���':8, u'��':9, u'���':10, u'��':11, u'���':12, u'��':13, u'���':14, u'����~~':15, u'�����':16}

for x in data:
    try:
        t = Teacher(id=x['teacherId'], name=x['teacherName'], title=x['teacherTitle'], email=x['teacherEmail'], position=x['teacherPosition'], department=Department.objects.get(id=departmentsMap[x['department']]))
    except UnicodeEncodeError:
        continue
        