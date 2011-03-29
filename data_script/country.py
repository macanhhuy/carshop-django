
#import file
import re

insertSql = '''
INSERT INTO parameter
	(`parameter_code`, `parameter_display_name`, `parameter_value`, `parameter_sequence`, `parameter_is_valid`, `time_parameter_created`)
VALUES
	('country', '''

def readCountry():
	#n = re.compile('\n')
	f = open('country.txt')
	countries = []
	sqlCountries = []
	for line in f:
		if len(line)>3:
			country = re.split(r'\t', line)
			country[1] = re.sub(r'\n', '', country[1])
			countries.append(country)
	f.close()
	
	f_sql = open('country.sql', 'w')
	for i in range(0, len(countries)):
		sql = insertSql
		sql += "'" + countries[i][1] + "', "
		sql += "'" + countries[i][0] + "', "
		sql += str(i+1)
		sql += ', 1, '
		sql += 'now());\n'
		f_sql.write(sql)
		
	f_sql.close()

readCountry()
	
	