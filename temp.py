# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib3

url="https://wwww.baidu.com"

def basicHTTP():
    http=urllib3.PoolManager()
    r=http.request('GET','http://www.baidu.com')
    print(r.status)
    print(r.data)
    
basicHTTP()