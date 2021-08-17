# When i got stuck I used https://knowledge.udacity.com/questions/195897#195955

import math
from queue import PriorityQueue
from helpers import load_map


def shortest_path(graph, starting_intersection, destiny_intersection):

    frontier = PriorityQueue()
    frontier.put(starting_intersection, 0)

    previous_intersections = {starting_intersection: None}
    path_costs = {starting_intersection: 0}

    while not frontier.empty():
        current_intersection = frontier.get()

        if current_intersection == destiny_intersection:
            generate_path(previous_intersections, starting_intersection, destiny_intersection)

        for intersection_index in graph.roads[current_intersection]:
            update_path_cost = path_costs[current_intersection] + euclidean_distance(graph.intersections[current_intersection], graph.intersections[intersection_index])

            if intersection_index not in path_costs or update_path_cost < path_costs[intersection_index]:
                path_costs[intersection_index] = update_path_cost
                path_cost_with_goal_distance = update_path_cost + euclidean_distance(graph.intersections[current_intersection], graph.intersections[intersection_index])

                frontier.put(intersection_index, path_cost_with_goal_distance)
                previous_intersections[intersection_index] = current_intersection

    return generate_path(previous_intersections, starting_intersection, destiny_intersection)


def euclidean_distance(intersection_a, intersection_b):
    """Calculates cartesian distance between two points for h-function."""

    return math.sqrt(((intersection_a[0] - intersection_b[0]) ** 2) + ((intersection_a[1] - intersection_b[1]) ** 2))


def generate_path(previous_intersections, starting_intersection, destiny_intersection):
    current_intersection = destiny_intersection
    best_path = [current_intersection]

    while current_intersection != starting_intersection:
        current_intersection = previous_intersections[current_intersection]
        best_path.append(current_intersection)

    best_path.reverse()

    return best_path



map_10 = load_map('map-10.pickle')
map_40 = load_map('map-40.pickle')

path = shortest_path(graph=map_40,
                     starting_intersection=8,
                     destiny_intersection=24)
assert path == [8, 14, 16, 37, 12, 17, 10, 24]
