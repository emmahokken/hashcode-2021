filename = 'data/a.txt'

def load_data(filename):
    lines = open(filename).readlines()
    print(lines)

    seconds, intersections, no_streets, cars, score = lines[0].split()

    simulation = Simulation(seconds, intersections, no_streets, cars, score)

    street_count = 0
    streets = []
    cars = []
    for line in lines[1:]:
        info = line.split()
        
        # if you can cast second to int, it is a street
        if street_count < int(no_streets):
            streets.append(Street(info[0], info[1], info[2], info[3]))
            street_count += 1
        else:
            car = Car(info[0])

            for street in info[1:]:
                car.add_path(street)
            cars.append(car)

    for street in streets:
        print(street)

    simulation.load_streets(streets)
    simulation.load_cars(cars)


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

    def step(self):
        self.check_if_any_car_reach_destination()
        
        self.update_traffic_lights()

        self.update_car_positions()

        self.current_time += 1



class Street():
    def __init__(self, intersect1, intersect2, name, length):
        self.i1 = intersect1
        self.i2 = intersect2

        self.green = False

        self.name = name
        self.length = length

    def __str__(self):
        return f"Street {self.name} from i {self.i1} to i {self.i2} of length {self.length}"


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

load_data(filename)