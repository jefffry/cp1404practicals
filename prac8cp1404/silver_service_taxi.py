from prac8cp1404.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return " {} plus flagfall of $4.50".format(super().__str__(),
                                                   self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall + super().get_fare()

