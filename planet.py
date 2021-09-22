#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:02:25 2021

@author: benjamim francisco

"""
import os
from dotenv import load_dotenv
import json
import pathlib
import time

import requests
from requests.auth import HTTPBasicAuth


load_dotenv()
apiKey = os.getenv('PLANET_API_KEY')
apiUrl = 'https://api.planet.com/compute/ops/orders/v2'
auth = HTTPBasicAuth(apiKey, '')
response = requests.get(apiUrl, auth=auth)

request = {  
   "name":"simple order",
   "products":[
      {  
         "item_ids":[  
            "20151119_025740_0c74",
            "20151119_025741_0c74"
         ],
         "item_type":"PSScene4Band",
         "product_bundle":"analytic"
      }
   ],
}
headers = {'content-type': 'application/json'}

def place_order(request, auth):
    response = requests.post(apiUrl, data=json.dumps(request), auth=auth, headers=headers)
    print(response)
    order_id = response.json()['id']
    print(order_id)
    order_url = apiUrl + '/' + order_id
    return order_url

order_url = place_order(request, auth)