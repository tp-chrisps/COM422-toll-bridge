from vehicle import Vehicle
class Lorry(Vehicle):
    def __init__(self, reg, weight):
        super().__init__(reg, weight)

    def CalculateFee(self) -> float:
        if self.weight > 8000:
            return float(15)
        return float(10)