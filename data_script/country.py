# coding: utf-8
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

#readCountry()

def replaceContent():
	f = open('country_a.txt')
	f_temp = open('country_temp.txt', 'w')

	for line in f:
		if line.startswith('    <optio'):
			line = line.replace('    <option value="', '')
			line = line.replace('">', '\t')
			line = line.replace('" selected="	', '\t')
			line = line.replace('&amp;', '&')
			line = line.replace(',', '')
			line = line.replace('</option>', '')
			f_temp.write(line)
	
	f.close()
	f_temp.close()
	


#replaceContent()
#https://www.chineselovelinks.com
requestUrlState1 = '''/extensions/data/getStates.cfm?countryCode='''
requestUrlState2 = '''&initialSelectionText=Select...&initialSelectionValue=&languageID=en_US'''

requestUrlCity1 = '''/extensions/data/getCities.cfm?countryCode='''
requestUrlCity2 = '''&stateCode='''
requestUrlCity3 = '''&initialSelectionText=Select...&initialSelectionValue=&languageID=en_US'''

import os
import httplib

def collectCity(conn, fileName, stateCode, stateName):
	f = open(fileName)
	for line in f:
		if line.startswith('	obj.options[o'):
			line = line.replace("obj.options[obj.options.length] = new Option('", '')
			line = line.replace("');", '')
			city = re.split("','", line)
			conn.request('GET', requestUrlCity1 + stateCode + requestUrlCity2 + city[1].replace('\n', '') + requestUrlCity3)
			result = conn.getresponse()
			data = result.read()
			f_city = open('./temp/' + stateCode + '/city_' + city[1].replace('\n', '') + '.txt', 'w')
			f_city.write(data)
			f_city.close()
			print("*state: %s, city: %s complete" %(stateName, city[0]))
	f.close()
	return

def collectState(conn):
	f = open('country_temp.txt')
	
	for line in f:
		c = re.split(r'\t', line)
		if not os.path.exists('./temp/' + str(c[0])):
			os.mkdir('./temp/' + str(c[0]))
		conn.request('GET', requestUrlState1 + str(c[0]) + requestUrlState2)
		result = conn.getresponse()
		data = result.read()
		f_temp = open('./temp/' + str(c[0]) + '/' + str(c[0]) + '.txt', 'w')
		f_temp.write(data)
		f_temp.close()
		collectCity(conn, './temp/' + str(c[0]) + '/' + str(c[0]) + '.txt', str(c[0]), str(c[1]).replace('\n', ''))
		print('complete: ' + str(c[0]) + ', ' + str(c[1]).replace('\n', ''))
	f.close()

def generateCountry():
	conn = httplib.HTTPConnection('www.chineselovelinks.com')
	collectState(conn)
	conn.close()
	print('all complete')



#generateCountry()



def generateIso():
	f_temp = open('country_temp.txt')
	f_iso = open('country_iso_a.txt')
	f_result = open('country_result.txt', 'w')

	iso_temp = f_iso.readlines()
	f_iso.close()

	for line in f_temp:
		c_temp = re.split('\t', line)
		isFind = False
		for iso_line in iso_temp:
			c_iso = re.split('\t', iso_line)
			#print('%s *** %s' %(c_iso[0].replace('\n', ''), c_temp[1].replace('\n', '')))
			if c_iso[0].replace('\n', '').find(c_temp[1].replace('\n', '')) >= 0:
				f_result.write(line.replace('\n', '') + '\t' + c_iso[1] + '\t' + c_iso[2] + '\n')
				isFind = True
				break
		if not isFind:
			f_result.write(line)

		print('complete: %s' %(c_temp[1]))

	f_result.close()
	
	f_temp.close()

#generateIso()

sql_country = """
INSERT INTO country_state_city
	(`name`, `country_iso_code_2`, `country_iso_code_3`, `sequence`, `is_valid`)
VALUES"""

sql_state_city = """
INSERT INTO country_state_city
	(`name`, `parent_id`, `sequence`, `is_valid`)
VALUES"""

def generateSql():
	dataCount = 1
	basePath = './temp/'
	f_result = open('country_result.txt')
	f_sql = open('country_sql.txt', 'w')
	
	result_content = f_result.readlines()
	f_result.close()
	
	for i in range(0, len(result_content)):
		country = re.split('\t', result_content[i].replace('\n', ''))
		print('start country: %s ' %(country[1]))
		if len(country) == 4:
			f_sql.write('/********** start country: %s **********/\n' %(country[1]))
			f_sql.write("%s ('%s', '%s', '%s', %s, %s);\n" %(sql_country, country[1], country[2], country[3], str(i+1), '1'))
		elif len(country) == 2:
			f_sql.write('/********** start %s **********/\n' %(country[1]))
			f_sql.write("%s ('%s', '%s', '%s', %s, %s);\n" %(sql_country, country[1], '', '', str(i+1), '0'))
		else:
			print(u'异常: %s' %(result_content[i]))
		
		dataCount += 1
		
		f_state = open(basePath + country[0] + '/' + country[0] + '.txt')
		index_state = 1
		for state_line in f_state:
			if state_line.startswith("	obj.options[obj.options.length] = new Option('"):
				state_line = state_line.replace("	obj.options[obj.options.length] = new Option('", '')
				state_line = state_line.replace("');\n", '')
				state = re.split("','", state_line)
				print('    start state: %s ' %(state[0]))
				f_sql.write('/*========= start state: %s =========*/\n' %(state[0]))
				f_sql.write("%s ('%s', (select csc.id from country_state_city as csc where csc.name='%s' and csc.parent_id is null), %s, %s);\n" %(sql_state_city, state[0], country[1], str(index_state), '1'))
				
				dataCount += 1
				f_sql.write('/*--------- start city ---------*/\n')
				f_city = open(basePath + country[0] + '/city_' + state[1] + '.txt')
				index_city = 1
				for city_line in f_city:
					if city_line.startswith("	obj.options[obj.options.length] = new Option('"):
						city_line = city_line.replace("	obj.options[obj.options.length] = new Option('", '')
						city = re.split("','", city_line)
						f_sql.write("%s ('%s', (select csc.id from country_state_city as csc where csc.name='%s' and csc.parent_id = (select csc1.id from country_state_city as csc1 where csc1.name='%s' and csc1.parent_id is null) limit 0,1), %s, %s);\n" %(sql_state_city, city[0], state[0], country[1], str(index_city), '1'))
						print('        city: %s OK' %(city[0]))
						dataCount += 1
						index_city += 1
				
				f_city.close()
				f_sql.write('/*--------- end city ---------*/\n')
				
				index_state += 1
				f_sql.write('/*========= end state: %s =========*/\n' %(state[0]))
				print('    end state: %s ' %(state[0]))
		f_state.close()
		

		f_sql.write('/********** end country: %s **********/\n' %(country[1]))
		print('end country: %s ' %(country[1]))
		print str(dataCount)
		
	f_sql.close()
	
#generateSql()	
	