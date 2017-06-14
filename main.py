import csv
#from json import *

def cat(note):
	name=list()
	nom=list()
	no=list()
	for i in note:
		i=i.split('/')
		for j in range(len(i)):
			t=True
			for l in range(len(name)):
				if i[j]==name[l] and nom[l]==j:
					t=False
					i[j]=l
			if t:
				name.append(i[j])
				nom.append(j)
				i[j]=len(nom)-1
		no.append(i)
	cate=dict()
	k=0
	for i in no:
		if k<len(i)-1:
			if i[k] not in cate.keys():
				cate[i[k]]=[]
		if 0<k<len(i):
			cate[i[k-1]].append(i[k])
	return no
	'''

		for j in range(len(i)-1):
			if i[j] not in cate.keys():

			t=True
			for l in cate.keys():
				if i[j] in l:
					t=False
			if t:
	'''
	'''
	cate=dict()
	no=list()
	for i in note:
		no.append(i.split('/'))
	for i in no:
		if i[0]
	return no
	'''
	'''
	for i in note:
		max=i.count('/')+1
	for i in note:
		no=i.split('/')
		if len(no)==max:
			no[max-1]
	'''
	'''
	for i in note:
		no=i.split('/')
		while len(no)>0:
			if no[0] in cate:
				cate.append()
	'''

while True:
	print('--------------------','1 - На сегодня','2 - Ветки','3 - Добавить','4 - ','0 - Выход',sep='\n')
	inp=int(input())
	if inp==0: break

	if inp==3:
		print('--------------------','1 - Датированное','2 - Ветка','3 - Не забыть',sep='\n')
		typ=int(input())
		while True:
			name=input('Дело: ')
			if name=='0': break
			unit=input('Узел: ') if typ==2 else 0
			time=input('Когда выполнить: ') if typ!=3 else 0
			with open('db.csv', 'a') as file:
				csv.writer(file, delimiter='|', quotechar=' ', quoting=csv.QUOTE_MINIMAL).writerow([name,time,unit,1])
			'''
			with open('db.txt', 'a') as file:
				print(dumps({'note':name,'unit':unit,'time':time}), file=file, end='')
			'''

	if inp==2:
		unit=list()
		with open('db.csv', 'r') as file:
			for i in csv.reader(file, delimiter='|', quotechar=' '):
				if i[2]:
					unit.append(i[2]+'/'+i[0])
		for i in cat(unit):
			for j in i:
				print(j,end='	')
			print()
		'''
		with open('db.txt', 'r') as file:
			print(loads(file.read()))
		'''
