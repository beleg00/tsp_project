# -*- coding: utf-8 -*-
"""
TSP - Local Search 
SS2024

Group: 3 Sandra,Johanna,Evgenii
"""

import utils
import random

# Tries to improve the route by swapping two customers. 
# The customers are selected randomly.
def make_dummy_ls(route, matrix):
    # Make a copy of the route
    copy_route = list(route)

    # Calculate its cost
    cost = utils.calc_cost(copy_route, matrix)        

    # Select two (different) random customers
    customer1 = random.randint(1, len(matrix) - 1)
    customer2 = random.randint(1, len(matrix) - 1)
    while customer2 == customer1:
        customer2 = random.randint(1, len(matrix) - 1)
        
    # Exchange them in the route
    copy_route[customer1], copy_route[customer2] = copy_route[customer2], copy_route[customer1]

    # Evaluate the solution now
    new_cost = utils.calc_cost(copy_route, matrix)
    
    # If the solution is better, return the improved route
    if new_cost < cost:
        return copy_route
    
    # If not, undo the exchange and continue searching for improvements
    else:
        return route


#  *** Segment shift local search heuristic strategy ***

def segment_shift(route, matrix, segment_length=2):
    best_route = route[:]
    best_cost = utils.calc_cost(best_route, matrix)
    
    improvement_found = True

    while improvement_found:
        improvement_found = False
        
        start_index = random.randint(1, len(route) - segment_length - 1)
        segment = route[start_index:start_index + segment_length]

        for i in range(1, len(route) - segment_length):
            new_route = route[:start_index] + route[start_index + segment_length:]
            new_route[i:i + segment_length] = segment  
            
            # making sure  the route ends at the depot correctly
            new_route = [new_route[0]] + new_route[1:-1] + [new_route[0]]
            
            new_cost = utils.calc_cost(new_route, matrix)
            
            if new_cost < best_cost:
                best_route = new_route[:]
                best_cost = new_cost
                improvement_found = True
                break  # stop the loop as soon as a better solution is found 

    return best_route





#Our heuristic strategy. It attempts to improve a given route by
# iteratively shifting segments of a specified length to different positions within the route
#The goal is to find a route with a lower cost


#We keep looping until we can't make the route any better. In each loop:

#We randomly pick a part of the route, called a segment.
#We try moving this segment to different spots in the route.
#After each move, we check how much it costs to travel this new route.
#If the cost of this new route is lower than what we've seen before, we keep it as our best route

















