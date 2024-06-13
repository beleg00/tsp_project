# -*- coding: utf-8 -*-
"""
TSP - Main file. 
SS2024

Group: 3 Evgenii, Johanna, Sandra
"""

# Import your modules here.
import tsp_construct_heuristics as c
import tsp_localsearch_heuristics as ls
import tsp_read_data as read
import plot
import utils

import time

# Main program.

# These are the instances you should be able to solve in the end.
instances = ['burma14.tsp', 'bays29.tsp', 'berlin52.tsp', 'bier127.tsp']
optima = {'burma14.tsp': 3323, 'bays29.tsp': 2020, 'berlin52.tsp': 7542, 'bier127.tsp': 118282}

# You can begin by solving the smallest one, and then try the rest when the code is working
# Comment the next line if you want to try all instances
instances = [instances[1]]  # Testing here by changing numbers (we tested all of them,looks correct :)

for instance in instances:
    print('\nSolving instance:', instance)

    # First, read instance data using the function in tsp_read_data.
    coordinates, matrix = read.read_instance(instance)

    # Measure optimization time
    start = time.time()

    # Second, build a solution to the TSP using in our case Farthest Insertion
    print('solving instance using Farthest Insertion Construction Heuristic:')
    fi_route = c.farthest_insertion(matrix)
    total_time_fi = time.time() - start
    print('Best route:', fi_route)
    fi_cost = utils.calc_cost(fi_route, matrix)
    print('Cost of the solution using Farthest Insertion Construction Heuristic:', fi_cost)
    print('Total time for Farthest Insertion Construction Heuristic:', total_time_fi)

    # Plot the initial route obtained by Farthest Insertion in our case 
    plot.plot_route_with_labels(fi_route, coordinates)

    # Third, improve that solution by using a local search (in our case Segment Shift)
    start = time.time()
    improved_route = ls.segment_shift(fi_route, matrix, segment_length=2)
    total_time_ls = time.time() - start

    improved_cost = utils.calc_cost(improved_route, matrix)
    
    # Calculating percentage reduction
    reduction = fi_cost - improved_cost
    percentage_reduction = (reduction / fi_cost) * 100
    
    
    # Some printing now
    print('Cost after optimization     :', improved_cost, "(", optima[instance], ")")
    print('Total time for local search :', total_time_ls)
    print('Percentage reduction        :', percentage_reduction, '%')

    
    
    # Plot the improved route after local search
    plot.plot_route_with_labels(improved_route, coordinates)

    # Using additional local search heuristics on improved_route
    print('using the additional local search heuristics')

    # Segment shift local search strategy
    start = time.time()
    segment_shift_route = ls.segment_shift(improved_route, matrix, segment_length=2)
    segment_shift_time = time.time() - start
    print('segment shift route:', segment_shift_route)
    print('Cost of segment shift solution:', utils.calc_cost(segment_shift_route, matrix))
    print('time for segment shift:', segment_shift_time)
    plot.plot_route_with_labels(segment_shift_route, coordinates)


