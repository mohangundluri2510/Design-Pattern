class Vehicle:
    """Initialize a Vehicle object with the specified attributes."""

    def __init__(self, wheels, seating_capacity, maximum_speed):
        self.wheels = wheels
        self.seating_capacity = seating_capacity
        self.maximum_speed = maximum_speed

    def display_attributes(self):
        # Display the attributes of the vehicle
        print(f"Wheels: {self.wheels}")
        print(f"Seating Capacity: {self.seating_capacity}")
        print(f"Maximum Speed: {self.maximum_speed}")


class Car(Vehicle):
    """Initialize a Car object."""
    def __init__(self):
        super().__init__(wheels=4, seating_capacity=4, maximum_speed=150)


class Motorcycle(Vehicle):
    """Initialize a Motorcycle object."""
    def __init__(self):
        super().__init__(wheels=2, seating_capacity=2, maximum_speed=130)


class Truck(Vehicle):
    """Initialize a Truck object."""
    def __init__(self):
        super().__init__(wheels=6, seating_capacity=2, maximum_speed=100)


class VehicleFactory:
    """Create and return a vehicle object based on the given vehicle type."""
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            # Create and return a Car object
            return Car()
        elif vehicle_type == "motorcycle":
            # Create and return a Motorcycle object
            return Motorcycle()
        elif vehicle_type == "truck":
            # Create and return a Truck object
            return Truck()
        else:
            # Raise an error for invalid vehicle types
            raise ValueError("Invalid vehicle type")


def main():
    # Get the desired vehicle type from user input
    manufacture_vehicle_type = input("Enter the type of vehicle you want to manufacture (car, motorcycle, or truck): ")

    # Create a VehicleF
    # factory object
    vehicle_factory = VehicleFactory()

    # Create the specified vehicle using the factory
    vehicle = vehicle_factory.create_vehicle(manufacture_vehicle_type)

    # Display the attributes of the created vehicle
    vehicle.display_attributes()


if __name__ == "__main__":
    main()
