import sys
f = open(sys.argv[1],"r")
#the columns are on the first line separated by ;
columns = f.readline().split(";");
objs = {}
rows = f.readlines();
for row in rows:
	fields = row.split(";")
	obj = {}
	for column in columns:
		obj[column.replace("\n","")] = fields[columns.index(column)].replace("\n","")	 
	objs[fields[0]] = obj
print objs
