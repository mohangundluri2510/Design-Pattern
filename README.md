## Design Pattern

<hr>

### Weather Monitering System
<p>The Weather Monitoring System is a Python program that enables real-time weather monitoring and 
updates to numerous display devices. It uses the Publish-Subscribe design pattern to create a one-to-many
relationship between the display devices (subscribers) and the weather station (publisher). 
Each registered display device receives an automatic notification from the weather station when fresh weather
data becomes available, and each device then updates its user interface to show the most recent weather data.</p>


- Created class **WeatherStation**
    - Description: Represents a weather station that collects and distributes weather data to subscribed display devices.
    - Methods:
      - subscribe(display_device, topic): Subscribes a display device to a specific topic.
      - unsubscribe(display_device, topic): Unsubscribes a display device from a specific topic.
      - publish(topic, message): Publishes a message to all subscribers of a specific topic.
    
- Created class **DisplayDevice**
  - Description: Abstract base class for display devices that receive weather data updates.
  - Methods:
    - update(message): Abstract method to be implemented by subclasses for updating the display device with the received message.
    


- Created class **MobileApp**
    - Description: Represents a mobile app display device that receives weather data updates.
    - Methods:
      - update(message): Implementation of the update method for the MobileApp display device.
- Created class **WebInterface**
  - Description: Represents a web interface display device that receives weather data updates.
  - Methods:
    - update(message): Implementation of the update method for the WebInterface display device.
- Created class **DesktopApplication**
    - Description: Represents a desktop application display device that receives weather data updates.
    - Methods:
      - update(message): Implementation of the update method for the DesktopApplication display device.


### Vehicle Manufacturing System

- Created class **Vehicle**
    - Description: Represents a generic vehicle with common attributes such as wheels, seating capacity, and maximum speed.
    -  Methods:
        - __init__(self, wheels, seating_capacity, maximum_speed): Initializes the Vehicle object with the specified attributes.
display_attributes(self): Displays the attributes of the vehicle.

- Created class **Car**
  - Description: Represents a car, a type of vehicle with specific attribute values.
  - Methods:
    - __init__(self): Initializes the Car object with predefined attribute values.

- Created class **Motorcycle**
    - Description: Represents a motorcycle, a type of vehicle with specific attribute values.
    - Methods:
      - __init__(self): Initializes the Motorcycle object with predefined attribute values.
- Created class **Truck**
  - Description: Represents a truck, a type of vehicle with specific attribute values.
  - Methods:
        - __init__(self): Initializes the Truck object with predefined attribute values.
- Created class **VehicleFactory**
     - Description: Factory class responsible for creating different types of vehicles.
       - Methods:
         - create_vehicle(vehicle_type): Creates and returns a vehicle object of the specified type.