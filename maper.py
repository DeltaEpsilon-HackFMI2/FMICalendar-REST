from schedule.models import *
import json

json_data = open('C:\\Users\\simeon.COMSOFTL\\Desktop\\HackFMI-backend\\FMICalendar-REST\\FMI-Data-master\\teachers.json','rb')

data = json.load(json_data)

departmentsMap={'Àëã': 1, 'ÀÌ':2, 'ÂÎÈÑ':3, 'Ãåîì':4, 'ÄÓ':5, 'ÈÑ':6, 'ÈÒ':7, 'ÊÀÒ':8, 'ÊÈ':9, 'ÌËÏ':10, 'ÌÀ':11, 'ÎÌÈ':12, 'ÑÒ':13, '×ÌÀ':14, 'ËÌÌÈ~~':15}

for x in data:
    try:
        t = Teacher(id=x['teacherId'], name=x['teacherName'], title=x['teacherTitle'], email=x['teacherEmail'])
    except UnicodeEncodeError:
        continue
