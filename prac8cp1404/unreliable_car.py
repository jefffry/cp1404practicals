import random
from prac8cp1404.Car import Car

class Unreliable_car(Car): #must be uppercase C no underline! <-- wrong name
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        percentage = random.uniform(0, 100) #just use random_number for the percentage
        if percentage > self.reliability:
            travel = 0
        else:
            travel = super().drive(distance)

        return travel
