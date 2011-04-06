# -*- coding:utf-8

import os
import re
import httplib



def requestMake():
	conn = httplib.HTTPConnection('www.covers4auto.com')
	conn.request('GET', '/shopbyvehicle.html')
	makePage = conn.getresponse()
	data = makePage.read()
	
	#f = open('page.html', 'w')
	#f.write(data)
	
	p = re.compile('<a href="make/.*.html" class="blue12">.*</a>')
	makeUrls = re.findall(p, data)
	
	f = open('makeUrl.txt', 'w')
	for makeUrl in makeUrls:
		f.write(makeUrl+'\n')
	
	f.close()

	

#requestMake()



def requestProduct():

	if not os.path.exists('./product_temp'):
		os.mkdir('./product_temp')
	
	conn = httplib.HTTPConnection('www.covers4auto.com')
	
	home_url = "www.covers4auto.com"
	home_replace_url = "{{ home_url }}"
	
	sql = '''
	INSERT INTO car_manufacturer(name, time_added, time_modified, manufacturer_desc)
	VALUES('%s', %s, %s, '%s');\n\n'''
	
	f_make = open('makeUrl.txt')
	p_name = re.compile('>.*<')
	p_url = re.compile('make/.*.html')
	
	f_product_sql = open('product.sql', 'w')
	
	for line in f_make:
		try:
			name = re.search(p_name, line)
			name = name.group(0)[1:-1]
			url = re.search(p_url,line)
			url = '/' + url.group(0)

			conn.request('GET', url)
			result = conn.getresponse()
			data = result.read()
			

			
			p_desc = re.compile(name + '</span>[\s\S]+?</td>')
			desc = re.search(p_desc, data)
			desc = desc.group(0)
		
			desc = desc.replace(name + '</span>', '')
			desc = desc.replace('          </td>', '')
			desc = desc.replace('www.covers4auto.com', '{{ home_url }}')
			desc = desc.replace("'", "\'")
		
			f_product_sql.write(sql %(name, 'now()', 'now()', desc))
		
		except Exception, e:
			print(e)
			f_product_sql.write(sql %(name, 'now()', 'now()', ''))
		
		print('%s complete' %(name))
		
		

	f_product_sql.close()
	f_make.close()
	
	
requestProduct()
	
	