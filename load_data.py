from collections import defaultdict 
import random

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

class Intersection():
    def __init__(self):
        self.streets = []

        self.scheduled = False

    def add_street(self, street):
        self.streets.append(street)

        
    def pick_light(self, street):
        for street in self.streets:
            street.traffic_light.
        street = random.choice(self.streets)

    def __str__(self):
        street_str = ""
        for street in self.streets:
            street_str +- street + "\n"
        return street_str


class Street():
    def __init__(self, intersect1, intersect2, name, length):
        self.i1 = intersect1
        self.i2 = intersect2

        self.name = name
        self.length = length

        self.traffic_light = TrafficLight()

    def __str__(self):
        return f"Street {self.name} from intersection {self.i1} to intersection {self.i2} of length {self.length}"


class TrafficLight():
    def __init__(self):
        self.green = False
        self.has_been_green = False
        
    def turn_green(self, time):
        self.green = True
        self.start = time 

    def turn_red(self, time):
        self.green = False
        self.has_been_green = True
        self.end = time


class Car():
    def __init__(self, start):
        self.start = start

        self.route = []

    def add_path(self, path):
        self.route.append(path)

    def set_starting_position(self):
        self.position = self.route[0]

    def reached_destination(self, end_time):
        if self.position == self.route[-1]:
            self.end_time = end_time
            self.destination = True

    def __str__(self):
        return f"I'm a car and I started here: {self.start} and now I'm here {self.position}. Destination: {self.destionation}"

load_data(filename)
