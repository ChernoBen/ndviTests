#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 15:47:44 2021

@author: fang
"""
import geopandas as gpd
from shapely.geometry import Point, Polygon
import fiona
import pandas as pd
from pyproj import CRS

crs=CRS('EPSG:4326')
gpd.io.file.fiona.drvsupport.supported_drivers['LIBKML'] = 'rw'
my_map = gpd.read_file('ufmt.kml', driver='LIBKML')
my_map