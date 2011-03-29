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
	f = open('country_temp.txt')




generateIso()
	