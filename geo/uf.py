#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:35:59 2021

@author: fang
"""

import geopandas as gpd
from shapely.geometry import Point, Polygon
import pandas as pd
import pyproj

pyproj.datadir.set_data_dir('/home/fang/Documentos/pythonScripts/geo')
gpd.io.file.fiona.drvsupport.supported_drivers['LIBKML'] = 'rw'
my_map = gpd.read_file('ufmt.kml', driver='LIBKML')
my_map