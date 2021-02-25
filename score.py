

def score(simulation):
    ''' For a car that finishes its path at time T, the awarded score is (F) points 
        (fixed award for finishing the path) and additionally (D - T): 
        one point for each second left when the car finished the path. '''

    score = 0
    for car in simulation.cars: 
        if car.destination:
            score += simulation.score_per_car + (simulation.sim_time - car.end_time)

    return score