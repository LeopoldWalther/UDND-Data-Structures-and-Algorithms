from helpers import load_map
import math

map_10 = load_map('map-10.pickle')
map_40 = load_map('map-40.pickle')


def shortest_path(M, start, goal):
    print("shortest path called")
    return


class AStarRoutePlanner(object):
    """ ... """

    def __init__(self, road_map, starting_intersection, destination_intersection):
        self.road_map = road_map
        self.current_intersection_index = starting_intersection
        self.destination_intersection_index = destination_intersection
        self.frontier = [starting_intersection]  # list of nodes, which represent the farthest paths explored
        self.explored = []  # list of nodes, which are in between the frontier nodes and the starting node
        self.unexplored = list(self.road_map.intersections.keys())  # list of nodes, which are beyond the frontier
        self.distances = [[9999 for x in range(len(self.road_map.intersections))] for x in range(len(self.road_map.intersections))]

    def euclidean_distance(self, intersection_index_a, intersection_index_b):
        """Calculates cartesian distance between two points for h-function."""

        intersection_a_x, intersection_a_y = self.get_intersection_coordinates(intersection_index_a)
        intersection_b_x, intersection_b_y = self.get_intersection_coordinates(intersection_index_b)

        euclidean_distance = math.sqrt(
            (intersection_b_x - intersection_a_x)**2 + (intersection_b_y - intersection_a_y)**2)

        return euclidean_distance

    def evaluation_function(self, next_intersection_index):
        """Sum of g-function (actual distance travelled) and h-function (euclidean distance to goal)."""

        # distance current intersection to next intersection
        g_function = self.euclidean_distance(self.current_intersection_index, next_intersection_index)
        # TODO: save calculated distances in self.distances ?

        # distance from next intersection to destiny
        h_function = self.euclidean_distance(next_intersection_index, self.destination_intersection_index)
        # TODO: save calculated distances in self.distances_to_destiny ? 

        return g_function + h_function

    def get_intersection_coordinates(self, intersection_index):
        """Returns the tuple containing the x and y coordinates of a the given intersection index."""
        return self.road_map.intersections[intersection_index]

    def get_intersection_roads(self, intersection_index):
        """Returns the list of roads connected to the given intersection index."""
        return self.road_map.roads[intersection_index]

    def explore(self):
        print(f'\n Start exploring: \n')
        # while self.destination_intersection not in self.explored:

        for intersection_index in self.road_map.roads[self.current_intersection_index]:

            # add roads of current intersection to frontier if not already in frontier or explored
            if intersection_index not in self.explored and intersection_index not in self.frontier:
                self.frontier.append(intersection_index)

            # calculate for each point the actual distance to travel and the euclidean distance from there to goal
            value = self.evaluation_function(intersection_index)

            print(f' Road: {intersection_index} '
                  f'with coordinates: {self.get_intersection_coordinates(intersection_index)} '
                  f'has function value: {value}')

        # remove current intersection from frontier and add to explored

        # make road with smallest value the new current intersection


# start = 2
# destiny = 6
# route_planner = AStarRoutePlanner(road_map=map_10, starting_intersection=start, destination_intersection=destiny)

start = 5
destiny = 34
# path=[5,16,37,12,34])
route_planner = AStarRoutePlanner(road_map=map_40, starting_intersection=start, destination_intersection=destiny)

start_coordinates = route_planner.get_intersection_coordinates(start)
print(f' Starting index: {start}')
print(f' Starting coordinates: {start_coordinates}')
start_roads = route_planner.get_intersection_roads(start)
route_planner.explore()

