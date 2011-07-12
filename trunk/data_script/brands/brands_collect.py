# -*- coding:utf-8 -*-

import os
import httplib
import re
import urllib

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
    
    re_brands_td = re.compile('<td valign=top>.+</td>', re.S)
    
    re_brands = re.compile('<a href="(.+?-cars.html)".+?>(.+?)</a>', re.S)

    brands_td = re.search(re_brands_td, data)
    
    if brands_td is not None:
        f_brands = open('brands.txt', 'w')
        brands = re.findall(re_brands, brands_td.group(0))
        for brand_url, brand_name in brands:
            print(brand_url, brand_name)
            f_brands.write('%s\t%s\n' %(brand_url, brand_name))
    
        f_brands.close()


def collect_single_brand():

    conn = httplib.HTTPConnection(home_url)
    
    f = open('brands.txt')
    
    re_models = re.compile('<td valign=top>.+?</td>', re.S)
    re_model = re.compile('href="(.+?-car-model.html)">(.+?)</a', re.S)
    for line in f:
        brand_url, brand_name = line.split('\t')
        brand_name = brand_name[:-1]
        
        if os.path.exists(brand_name + '.txt'):
            print('jump: %s, %s' %(brand_url, brand_name))
            continue

        print('begin: %s, %s' %(brand_url, brand_name))
        conn.request('GET', urllib.quote(brand_url))
        result = conn.getresponse()
        data = result.read()

        m_models = re.search(re_models, data)

        f_model = open(brand_name + '.txt', 'w')
        if m_models is not None:
            models = re.findall(re_model, m_models.group(0))
            for (detail_url, detail_name) in models:
                f_model.write('%s\t%s\n' %(detail_url, detail_name))
        
        f_model.close()
        
        print('end: %s, %s' %(brand_url, brand_name))
    f.close()
    conn.close()


def collect_detail():
    conn = httplib.HTTPConnection(home_url)

    f = open('brands.txt')
    
    for line in f:
        brand_url, brand_name = line.split('\t')
        brand_name = brand_name[:-1]
        
        f_brand = open(brand_name + '.txt')
        for brand in f_brand:
            detail_url, detail_name = brand.split('\t')
            detail_name = detail_name[:-1]

            if not os.path.exists(brand_name):
                os.mkdir(brand_name)
            
            if os.path.exists(brand_name + '/' + detail_name + '.txt'):
                print('jump: %s, %s' %(detail_url, detail_name))
                continue

            print('begin: %s, %s' %(detail_url, detail_name))
            conn.request('GET', urllib.quote(detail_url))
            result = conn.getresponse()
            data = result.read()

            f_detail = open(brand_name + '/' + detail_name + '.txt', 'w')
            
            re_detail_items = re.compile('<b>(.+?)</table>', re.S)
            re_detail_item = re.compile('(.+?)</b>.+?<tr><td>(.+?)</td><td>(.+?)</td></tr>.+?<tr><td>(.+?)</td><td>(.+?)</td></tr>.+?<tr><td>(.+?)</td><td>(.+?)</td></tr>.+?<tr><td>(.+?)</td><td>(.+?)</td></tr>.+?<tr><td>(.+?)</td><td>(.+?)</td></tr>.+?<tr><td>(.+?)</td><td>(.+?)</td></tr>.+?<tr><td>(.+?)</td><td>(.+?)</td></tr>.+?<tr><td>(.+?)</td><td>(.+?)</td></tr>.+?<tr><td>(.+?)</td><td>(.+?)</td></tr>.+?<tr><td>(.+?)</td><td>(.+?)</td></tr>', re.S)

            detail_items = re.findall(re_detail_items, data)
            if detail_items is not None:
                for detail_item in detail_items:
                    detail_item_array = re.findall(re_detail_item, detail_item)
                    
                    if detail_item_array is not None:
                        
                        f_detail.write('\ndetail:\n')
                        #f_detail.write(detail_item_values[0] + '\n')
                        for detail_item_values in detail_item_array:
                            print('save detail: %s' %(detail_item_values[0]))
                            for detail_item_value in detail_item_values:
                                f_detail.write(detail_item_value + '\n')

            f_detail.close()
            
        f_brand.close()

    conn.close()

    print('end')

if __name__ == '__main__':
    #collect()
    #collect_single_brand()
    collect_detail()

