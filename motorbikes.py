from vehicle import Vehicle
class Motorbike(Vehicle):
    def __init__(self, reg:str, weight:int):
       super().__init__(reg, weight)

    def CalculateFee(self):
        fee = (3)
        return float(fee)
