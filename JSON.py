# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:09:46 2022

@author: Olivia
"""

import json
import requests


def topArticles(limit):
    pageNumber = limit
    URL = 'https://jsonmock.hackerrank.com/api/articles?page=<'+str(pageNumber)+'>'
    r = requests.get('https://jsonmock.hackerrank.com/api/articles?page=<1>')
    j = r.json()
    x = j['data']
    artiledict = {}
    dict_new ={}
    for i in range(0,len(x)):
        y = j['data'][i]
        if y['title'] == 0:
            title_s = y['storytitle']
            comments = y['num_comments']
            
        else:
            title_s = y['title']
            comments = y['num_comments']
        artiledict[i]=[title_s,comments]
        print(artiledict)
        
        
    #dict_new = sorted(artiledict[])
    print(dict_new)
    return artiledict    

x=topArticles(1)
print(x)
    
    