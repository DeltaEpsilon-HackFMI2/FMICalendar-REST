from schedule.models import *
import json

json_data = open('C:\\Users\\simeon.COMSOFTL\\Desktop\\HackFMI-backend\\FMICalendar-REST\\FMI-Data-master\\teachers.json','rb')

data = json.load(json_data)

departmentsMap={u'Àëã': 1, u'ÀÌ':2, u'ÂÎÈÑ':3, u'Ãåîì':4, u'ÄÓ':5, u'ÈÑ':6, u'ÈÒ':7, u'ÊÀÒ':8, u'ÊÈ':9, u'ÌËÏ':10, u'ÌÀ':11, u'ÎÌÈ':12, u'ÑÒ':13, u'×ÌÀ':14, u'ËÌÌÈ~~':15, u'Íåîïğ':16}

for x in data:
    try:
        t = Teacher(id=x['teacherId'], name=x['teacherName'], title=x['teacherTitle'], email=x['teacherEmail'], position=x['teacherPosition'], department=Department.objects.get(id=departmentsMap[x['department']]))
    except UnicodeEncodeError:
        continue
        