# -*- coding: utf-8 -*-
"""
TSP - Construction Heuristic
SS2024

Group: 3 Johanna,Sandra,Evgenii
"""
# Travelling Salesman Problem (T S P)

import random

def make_dummy_route(matrix):
    
    num_cities = len(matrix)
    route = [0]
    remaining_cities = [i for i in range(1, num_cities)]
    random.shuffle(remaining_cities)
    route.extend(remaining_cities)
    # Return to the depot
    route.append(0)
    return route

#This function generates a dummy route for solving the traveling salesman problem (TSP). 
#The route starts at the depot, which is city number 0.
#It mixes up the order of the other cities randomly
#after mixing, it adds the depot (city number 0) again at the end to make a complete loop
#Finally, it gives back the route as a list



# **** Farthest  inseration ***
import numpy as np

def farthest_insertion(matrix):
    n = len(matrix)
    route = [0]
    unvisited = list(range(1, n))

    while unvisited:
        farthest_point = max(unvisited, key=lambda x: min(matrix[x][p] for p in route))
        min_increase = np.inf
        best_position = None

        for i in range(1, len(route)):
            increase = matrix[route[i-1]][farthest_point] + matrix[farthest_point][route[i]] - matrix[route[i-1]][route[i]]
            if increase < min_increase:
                min_increase = increase
                best_position = i

        if best_position is None:
            best_position = len(route)
        
        route.insert(best_position, farthest_point)
        unvisited.remove(farthest_point)

    route.append(route[0])
    return route


"""
It starts with the first city (depot) and a list of unvisited cities.
each time, it picks the farthest city from the current route
It inserts this city into the route at the spot that adds the least extra distance
It repeats this until all cities are included in the route.
The function uses NumPy (imported as np) to handle matrix operations efficiently, making it easier to find good solutions

"""













