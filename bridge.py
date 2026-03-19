class Bridge:
    def __init__(self, max_size:int=20):
        self.vehicle_list = []
        self.max_size = max_size

    def calcTotalWeight(self) -> int:
        totalWeight = 0
        for vehicle in self.vehicle_list:
            totalWeight += vehicle.weight
        return totalWeight

    def addVehicle(self, vehicle: object) -> bool:
        if len(self.vehicle_list) < self.max_size:
            if self.calcTotalWeight() + vehicle.weight > 30000:
                return False
            self.vehicle_list.append(vehicle)
            return True
        else:
            return False

    def removeVehicle(self, reg: str) -> bool:
        for vehicle in self.vehicle_list:
            if vehicle.reg == reg:
                self.vehicle_list.remove(vehicle)
                return True
        return False