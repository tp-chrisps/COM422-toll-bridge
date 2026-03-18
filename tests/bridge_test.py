from bridge import Bridge
from cars import Cars

def test_create_bridge_unit():
    bridge = Bridge()
    assert bridge.max_size == 20 and bridge.vehicle_list == []


def test_bridge_calcTotalWeight_unit():
    car1 = Cars("abc", 1500)
    car2 = Cars("abc", 2000)
    bridge = Bridge()
    bridge.addVehicle(car1)
    bridge.addVehicle(car2)
    assert bridge.calcTotalWeight() == 3500

def test_bridge_remove_car():
    car1 = Cars("abc", 1500)
    car2 = Cars("bcd", 2000)
    bridge = Bridge()
    bridge.addVehicle(car1)
    bridge.addVehicle(car2)
    bridge.removeVehicle("bcd")
    assert car2 not in bridge.vehicle_list