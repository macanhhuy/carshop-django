# -*- coding:utf-8 -*-

import os
import httplib
import re

'''
http://www.drnew.com/car-brands.html
http://www.autoheroes.com/resources/manufacturers.shtml
http://buddysurvey4u.com/search/transport-newcars/index.htm
http://weblivenews.com/sports-car-brands-list/25096/
'''

home_url = 'www.drnew.com'

def collect():
	
    conn = httplib.HTTPConnection(home_url)
    conn.request('GET', '/car-brands.html')
    result = conn.getresponse()
    data = result.read()
    conn.close()
    
    re_brands = re.compile('<a href=".+?-cars.html" title=.+?</a>')
    brands = re.findall(re_brands, data)
    
    f_brands = open('brands.txt', 'w')
    for brand in brands:
        pass

    


if __name__ == '__main__':
    collect()


