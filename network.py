'''
Overall idea:
I made this project to practice implementing the A* algorithm. The scenario I am simulating is pretty arbitrary, but I chose it because it seemed interesting to implement.
The motivation is that a city planner wants to create a network of n settlements, such that the longest travel time in the network doesn't exceed d days.
This program is a tool that takes in n, d as parameters and plots a possible network that meets the requirements.

A link between two settlements is characterized by a distance s and a road condition c. Travel between two settlements takes d/100 * c days
'''


import numpy as np
from pathlib import Path
import random
import argparse
import math
import sys
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch


#Define road parameters
road_types = {0: "unclaimed", 1: 'trail', 2: 'gravel', 3: 'paved'}
road_condition = {'unclaimed': 5, 'trail': 2, 'gravel': 0.5, 'paved': 0.2}

#Helper to convert a csv to an array
def csvToArray(path):
    data = np.genfromtxt(path, delimiter = ',')
    return data

def minDistance(dist, sptSet, n):
        # Initialize minimum distance for next node
        min = sys.maxsize
        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(n):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
        return min_index

def graph_length(graph, n):
    longest = -sys.maxsize
    for src in range(n):
        dist = [sys.maxsize] * n
        dist[src] = 0
        sptSet = [False] * n

        for cout in range(n):
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = minDistance(dist, sptSet, n)
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(n):
                if graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + graph[x][y]:
                    dist[y] = dist[x] + graph[x][y]
        longest = max(longest, max(dist))
    return longest

def get_road_conditions(roads, n):
    road_conditions = np.zeros_like(roads).astype(object)
    for i in range(n):
        for j in range(n):
            road_conditions[i][j] = road_condition[road_types[roads[i][j]]]
    return road_conditions

def generate_graph(distances, roads, days, n):
    #Find the longest travel time of the current graph using A*
    road_conditions = get_road_conditions(roads, n)
    day_graph = np.multiply(distances/100, road_conditions)
    cur_days = graph_length(day_graph, n)
    #If it is too long, add a random road! (This isn't smart, but, oh well. I made this program to practice)
    type_to_change = 0 #change unpaved roads first
    while (cur_days>days):
        possible_roads = (roads==type_to_change).nonzero()
        while (len(possible_roads[0]) == 0):
            type_to_change +=1
            if(type_to_change==4):
                print("This isn't possible with current road technology!")
                break
            possible_roads = (roads==type_to_change).nonzero()
        chosen_road = random.randint(0, len(possible_roads[0])-1)

        x = possible_roads[0][chosen_road]
        y = possible_roads[1][chosen_road]
        roads = generate_a_random_road(roads, x, y)
        #Check if the longest travel time is shorter now
        road_conditions = get_road_conditions(roads, n)

        day_graph = np.multiply(distances/100, road_conditions)
        cur_days = graph_length(day_graph, n)
        print("Current days needed: ", cur_days)
    return roads, cur_days

def generate_a_random_road(roads, x, y):
    #Start with a random road condition
    
    type = random.randint(roads[x][y]+1,3)
    roads[x][y] = type
    return roads

#Plot the final settlement!
def plotter(x, y, roads, days):
    trails =  (roads==1).nonzero()
    gravel =  (roads==2).nonzero()
    paved =  (roads==3).nonzero()
    paths = [trails, gravel, paved]
    style = 0
    colors = ['green', 'yellow', 'red']
    lines = [1,1,1]
    for path in paths:
        for edge in range(len(path[0])):
            x_values = [x[path[0][edge]], x[path[1][edge]]]
            y_values = [y[path[0][edge]], y[path[1][edge]]]
            plt.plot(x_values, y_values, colors[style], linewidth = lines[style])
        style +=1
    plt.plot(x, y, 'o', color='blue')
    plt.title('Maximum distance between settlements is {} days'.format(days))
    plt.xlabel('X location(Km)')
    plt.ylabel('Y location(Km)')
    legend_elements = [Line2D([0], [0], color='green', lw=1, label='Trail'),
                   Line2D([0], [0], marker='o', color='w', label='Settlement',
                          markerfacecolor='blue', markersize=5),
                   Line2D([0], [0], color='yellow', lw=1, label='Gravel Road'),
                   Line2D([0], [0], color='red', lw=1, label='Paved Road')]
    plt.legend(handles = legend_elements)
    plt.show()
    

def generate(args):
    if  int(args.days)==0:
        print("Can't make the desired topology!")
        return
    else:
        days = int(args.days)
        n = int(args.settlements)
        #To start, randomize the settlement locations
        x_locs = np.random.rand(n) * args.x
        y_locs = np.random.rand(n) * args.y

        #Convert the locations to a 2d array of distances
        distances = np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                distances[i][j] = math.sqrt(math.pow((x_locs[i]-x_locs[j]), 2) + math.pow((y_locs[i]-y_locs[j]), 2))
        #Since all starting roads are unclaimed:
        roads = np.zeros_like(distances).astype(int)
        #Now, call an A* algorithm to make the template into a network that meets requirements!
        roads, cur_days = generate_graph(distances, roads, days, n)
        plotter(x_locs, y_locs, roads, round(cur_days*100)/100)
        return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-days", "--days", dest = "days", default = 7,  help="num maximum travel days")
    parser.add_argument("-x", "--xrange", dest = "x", default = 1500,  help="x distance of settlement area")
    parser.add_argument("-y", "--yrange", dest = "y", default = 1500,  help="y distance of settlement area")
    parser.add_argument('-n', '--num_settlements', dest = 'settlements', default = 5, help = 'number of settlements in network')
    parser.add_argument('-p', '--path', dest = 'path', default = "../Test_CSVs/Testing/", help = 'output folder path')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = main()
    generate(args)


