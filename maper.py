teachers_list = []
teachers_list_al = []

TEACHER_TAG = "teacherName"
TEACHER_TAG_AL = "teacher"

teachers = open('FMI-Data/teachers.json','r')
teachers_al = open('FMI-Data/program_cs.json','r')

for line in teachers:
	if TEACHER_TAG in line:
		a = line.strip()[16:-2].split(" ")
		teachers_list.append(a[0][0:2]+'.'+a[-1])


for line in teachers_al:
	if TEACHER_TAG_AL in line:
		a = line.strip()[12:]
		a = line.strip()[16:-2].split(" ")
		teachers_list.append(a[0][0:2]+'.'+a[-1])


for a in teachers_list:
	print a