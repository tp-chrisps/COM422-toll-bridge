from vehicle import vehicle

class Cars(vehicle):
    def __init__(self, reg, weight):
        super().__init__(reg, weight)

    def calculateFee(self):
        fee = float(5)
        while self.weight > 1590:
            fee += 0.1
            self.weight -= 100
        return fee