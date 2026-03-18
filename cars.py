from vehicle import Vehicle

class Cars(Vehicle):
    def __init__(self, reg, weight):
        super().__init__(reg, weight)

    def calculateFee(self):
        feeWeight = self.weight - 1590
        if feeWeight > 0:
            feeWeight = feeWeight // 100
            fee = 5 + (feeWeight / 10)
            return fee
        else:
            return 5



