def display_title():
    print("Welcome to the Toll Bridge")

def vehicle_options():
    print("Please select what vehicle you are driving today")
    print("[A] Car")
    print("[B] Motorbike")
    print("[C] Lorry")
    print("[X] Exit")
    print()
    option = input("Please select your option: ") .upper()
    print()
    return option


def weight_menu():
    if vehicle_options() == "A":
        int(input("Please enter the weight of your car"))
    elif vehicle_options() == "B":
        int(input("Please enter the weight of your motorbike"))
    elif vehicle_options() == "C":
        int(input("Please enter the weight of your Lorry"))
        option = input("Please select your option: ") .upper()
        print()
        return option
    return None

def register_vehicle():
    reg = input("Please enter your registration number: ")
    print(reg)













