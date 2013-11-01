from schedule.models import *
import json

json_data = open('C:\\Users\\simeon.COMSOFTL\\Desktop\\HackFMI-backend\\FMICalendar-REST\\FMI-Data-master\\teachers.json','rb')

data = json.load(json_data)

departmentsMap={'���': 1, '��':2, '����':3, '����':4, '��':5, '��':6, '��':7, '���':8, '��':9, '���':10, '��':11, '���':12, '��':13, '���':14, '����~~':15}

for x in data:
    try:
        t = Teacher(id=x['teacherId'], name=x['teacherName'], title=x['teacherTitle'], email=x['teacherEmail'])
    except UnicodeEncodeError:
        continue
