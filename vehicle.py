class Vehicle:
    def __init__(self, reg: str, weight: int):
        self.reg = reg
        self.weight = weight

    def CalculateFee(self) -> float:
        return self.weight / 100