#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:05:28 2021

@author: fang
"""

import requests
import json

'''
Agromonitoring api key
89572f5d18c309a566f85d2aec308733
endpoint = http://api.agromonitoring.com/agro/1.0/polygons?appid=test
'''
url = 'http://api.agromonitoring.com/agro/1.0/polygons?appid=89572f5d18c309a566f85d2aec308733'
custom_header = {'Content-Type':'application/json'}
body = {
   "name":"Exemplo",
   "geo_json":{
      "type":"Feature",
      "properties":{

      },
      "geometry":{
         "type":"Polygon",
         "coordinates":[
            [
                [
                  -412.3179068,
                  15.8669433
                ],
                [
                    -412.3112945,
                    15.8830007
                ],
                [
                  -412.2944633,
                  15.8780887
                ],
                [
                  -412.3075161,
                  15.8629804
                ],
                [
                  -412.3179068,
                  15.8669433
                ]
            ]
         ]
      }
   }
}
response = requests.post(url,headers=custom_header,data=body)

#response = requests.post(url,headers=custom_header,data=body)
#content = json.loads(response.content)