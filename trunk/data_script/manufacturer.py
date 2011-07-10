
f = open('manufacturer.txt')
f_sql = open('manufacturer_sql.txt', 'w')
for line in f:
	f_sql.write("insert into manufacturer (manufacturer_name, time_added, time_modified) value ('%s', now(), now());\n\n" %(line))
	
f.close()
f_sql.close()