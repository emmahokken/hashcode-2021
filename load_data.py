from collections import defaultdict 
import random

from classes import Car, TrafficLight, Intersection

filename = 'data/a.txt'

def load_data(filename):
    lines = open(filename).readlines()
    print(lines)

    seconds, intersections, no_streets, cars, score = lines[0].split()

    simulation = Simulation(seconds, intersections, no_streets, cars, score)

    street_count = 0
    streets = []
    cars = []
    intersections = defaultdict(Intersection)

    for line in lines[1:]:
        info = line.split()
        
        # if you can cast second to int, it is a street
        if street_count < int(no_streets):
            print(info[0], info[1], info[2], info[3])
            street = Street(info[0], info[1], info[2], info[3])
            streets.append(street)
            street_count += 1
            intersections[info[1]].add_street(street)
        else:
            car = Car(info[0])

            for street in info[1:]:
                car.add_path(street)
            cars.append(car)
    
    for street in streets:
        print(street)

    print(intersections['1'])

    simulation.load_streets(streets)
    simulation.load_cars(cars)
    # simulation.load_intersections(intersections)


class Simulation():
    def __init__(self, seconds, intersections, no_streets, no_cars, score):
        self.sim_time = seconds
        self.no_insects = intersections
        self.no_streets = no_streets
        self.no_cars = no_cars
        self.score_per_car = score

        self.current_time = 0

    def load_streets(self, streets):
        self.streets = streets

    def load_intersections(self, intersections):
        self.intersections = intersections

    def load_cars(self, cars):
        self.cars = cars

        for car in self.cars:
            car.set_starting_position()

    def check_if_any_car_reached_destination(self):
        for car in self.cars:
            car.reached_destination(self.current_time)

            # remove car from list?

    def update_traffic_lights(self):
        pass

    def update_car_positions(self):
        pass

    def count_intersections_scheduled(self):
        intersections_scheduled = 0
        for intersection in self.intersections:
            if intersection.scheduled:
                intersections_scheduled += 1
        return intersections_scheduled

    def write_out_file(self):
        intersections_scheduled = self.count_intersections_scheduled()

        assert intersections_scheduled <= self.no_insects, 'something went wrong with counting'

        with open('./results/' + self.version + '.txt', w) as resultsFile:
            writer = csv.writer(resultsFile)
            writer.writerow([intersections_scheduled])
        
        for intersection in self.intersections:
            for street in intersection.streets:
                if street.traffic_light.has_been_green() or street.traffic_light.green():
                    # write traffic lights in order

    def step(self):
        self.check_if_any_car_reach_destination()
        
        self.update_traffic_lights()

        self.update_car_positions()

        self.current_time += 1


load_data(filename)
