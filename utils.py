# -*- coding: utf-8 -*-
"""
Simple functions.
"""

import math

PI = 3.141592
RRR = 6378.388

def calc_cost(route, matrix):
    cost = 0
    for i in range(len(route)-1):
        cost += matrix[route[i]][route[i+1]]
    return cost


def coordinates2radians(x, y):
    deg = int(x)
    minutes = x - deg
    latitude = PI * (deg + 5.0 * minutes / 3.0) / 180.0
    
    deg = int(y)
    minutes = y - deg
    longitude = PI * (deg + 5.0 * minutes/ 3.0) / 180.0
    
    return latitude, longitude
    
    
def euc_dist(p1,p2):
    x1, y1 = p1
    x2, y2 = p2
    dist = ((x1-x2)**2+(y1-y2)**2)**0.5
    return dist
    
    
def geo_distance(coord_i, coord_j):
    lat_i, long_i = coord_i
    lat_j, long_j = coord_j
    
    q1 = math.cos(long_i - long_j)
    q2 = math.cos(lat_i - lat_j)
    q3 = math.cos(lat_i + lat_j)
    return RRR * math.acos(.5 * ((1.0+q1)*q2 - (1.0-q1)*q3))+1.0
    
    
def make_matrix(coordinates):
    matrix = []
    for c1 in coordinates:
        row = []
        for c2 in coordinates:
            d = euc_dist(c1, c2)
            row.append(d)
        matrix.append(row)
    return matrix
    