from cars import Cars
from lorry import Lorry
from motorbikes import Motorbike
from bridge import Bridge

def test_add_multiple_vehicles():
    car = Cars("abc", 1600)
    motorbike = Motorbike("def", 300)
    lorry = Lorry("ghi", 7900)
    bridge = Bridge()
    bridge.addVehicle(car)
    bridge.addVehicle(motorbike)
    bridge.addVehicle(lorry)
    assert bridge.calcTotalWeight() == 9800
