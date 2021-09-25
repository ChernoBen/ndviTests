#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 08:39:14 2021

@author: fang
"""
'''
Agromonitoring api key
89572f5d18c309a566f85d2aec308733
'''
import requests
import rasterio
from rasterio.plot import show
import numpy as np
from tqdm import tqdm

r = requests.get("http://api.agromonitoring.com/agro/1.0/polygons/61433c5ea2361700071b7084?appid=89572f5d18c309a566f85d2aec308733"
                  )
polygon = r.json()
#consulta ndvi
url = 'http://api.agromonitoring.com/agro/1.0/image/search?start=1500336000&end=1508976000&polyid=61433c5ea2361700071b7084&appid=89572f5d18c309a566f85d2aec308733'
content = requests.get(url)
data = content.json()
gallery = []
[ gallery.append(item['data']['ndvi']) for item in data ]

#test imagem na primeira posição
imgUrl = requests.get(gallery[6], stream=True)

with open("test.tiff", "wb") as handle:
    for data in tqdm(imgUrl.iter_content()):
        handle.write(data)
raster = rasterio.open('test.tiff')
show(raster)
show(raster.read()[0], cmap='summer')