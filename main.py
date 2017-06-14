import csv

def cat(note):
	name=list()
	nom=list()
	no=list()
	ma=0
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
		if len(i)>ma:
			ma=len(i)
	cate=dict()
	for k in range(ma):
		for i in no:
			if k<len(i):
				if i[k] not in cate.keys():
					cate[i[k]]=[]
			if 0<k<len(i):
				if i[k] not in cate[i[k-1]]:
					cate[i[k-1]].append(i[k])
			k+=1
	return cate

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

	if inp==2:
		unit=list()
		with open('db.csv', 'r') as file:
			for i in csv.reader(file, delimiter='|', quotechar=' '):
				if i[2]:
					unit.append(i[2]+'/'+i[0])
		note=cat(unit)
		on=list()
		for i in note:
			t=True
			for j in note[i]:
				if i==j:
					t=False
			if t:
				on.append(i)
		for i in on:
			print(i)
			print(j for j in note[i])