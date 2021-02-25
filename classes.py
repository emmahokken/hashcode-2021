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