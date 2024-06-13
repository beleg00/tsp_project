# -*- coding: utf-8 -*-
"""
Plotting function.
"""
import matplotlib.pyplot as plt

def plot_route_with_labels(route, coordinates, color = 'r', save_to_file = False, filename = 'route_labels1.pdf'):
    fig = plt.figure()
    labels = [label for label in range(len(coordinates))]
    x = [x for x, _ in coordinates]
    y = [y for _, y in coordinates]    
    route_x = [x[i] for i in route]
    route_y = [y[i] for i in route]
    plt.plot(route_x, route_y, color + 'o-')
    plt.plot(route_x[0], route_y[0], 'gs')
    no_x = [x for i, (x, y) in enumerate(coordinates) if i not in route]
    no_y = [y for i, (x, y) in enumerate(coordinates) if i not in route]
    plt.plot(no_x, no_y, 'bx')
    for i, c in enumerate(coordinates):
        x, y = c
        name = labels[i]
        plt.text(x, y, name)
    plt.margins(0.3)
    if save_to_file:
        plt.savefig(filename)
    else:
        plt.show()  






