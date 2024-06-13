# -*- coding: utf-8 -*-
"""
This file contains all functions related to how you read your data. 
"""

import math
import utils

def read_instance(filename):
    x = []
    y = []
    distances = []

    # read data file
    with open('INSTANCES/' +filename, 'r') as f:
            
            # skip 3 first lines
            next(f)
            next(f)
            next(f)
    
            # read dimension
            line = f.readline()
            dim = int(line.split(':')[1])
    
            # get weight type
            line = f.readline()
            weight_type = line.split(':')[1]
            weight_type = weight_type.lstrip()
            weight_type = weight_type.rstrip('\n')
            
            if(weight_type == 'EUC_2D'):
                # skip node coord section line
                next(f)
    
                for line in f:
                    if not line.startswith('EOF'):
                        words = line.split()
                        if len(words) > 2:
                            #print(line)
                            x.append(float(words[1]))
                            y.append(float(words[2]))
                        
                # calculate distance matrix
                for i in range(0, dim):
                    row = []
                    for j in range(0, dim):
                        dist = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
                        # row.append(int(dist))
                        row.append(int(dist+0.5))
                    distances.append(row)                
            
            elif(weight_type == 'GEO'):
                next(f)
                next(f)
                next(f)
    
                for i in range(dim):
                    line = f.readline()
                    words = line.split()
                    x.append(float(words[1]))
                    y.append(float(words[2]))
                
                # calc geo distance
                for i in range(dim):
                    coord_i = utils.coordinates2radians(x[i], y[i])
                    
                    row = []
                    for j in range(0, dim):
                        coord_j = utils.coordinates2radians(x[j], y[j])
                        dist = utils.geo_distance(coord_i, coord_j)
                        row.append(int(dist))
                    distances.append(row)
                
            elif(weight_type == 'EXPLICIT'):
                # skip lines
                next(f)
                next(f)
                next(f)
                
                for i in range(dim):
                    line = f.readline()
                    if not line.startswith('EOF'):
                        words = line.split()
                        row = []
                        for word in words:
                            row.append(int(word))
                        distances.append(row)
                
                # skip display data section line
                next(f)
                
                for i in range(dim):
                    line = f.readline()
                    words = line.split()
                    if len(words) > 2:
                        #print(line)
                        x.append(float(words[1]))
                        y.append(float(words[2]))
                
    
            return [e for e in zip(x, y)], distances

            