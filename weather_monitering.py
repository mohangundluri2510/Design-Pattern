class WeatherStation:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, display_device, topic):
        """Subscribe a display device to a specific topic."""

        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(display_device)

    def unsubscribe(self, display_device, topic):
        """Unsubscribe a display device from a specific topic."""
        if topic in self.subscribers:
            self.subscribers[topic].remove(display_device)

    def publish(self, topic, message):
        """Publish a message to all subscribers of a specific topic."""
        if topic in self.subscribers:
            for display_device in self.subscribers[topic]:
                display_device.update(message)


class DisplayDevice:
    def update(self, message):
        """Update method to be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement the update method")


class MobileApp(DisplayDevice):
    def update(self, message):
        """Update method for the MobileApp display device."""
        print(f"Mobile App received message: {message}")


class WebInterface(DisplayDevice):
    def update(self, message):
        """Update method for the WebInterface display device."""
        print(f"Web Interface received message: {message}")


class DesktopApplication(DisplayDevice):
    def update(self, message):
        """Update method for the DesktopApplication display device."""

        print(f"Desktop Application received message: {message}")


def main():
    weather_station = WeatherStation()

    mobile_app = MobileApp()
    web_interface = WebInterface()
    desktop_app = DesktopApplication()

    weather_station.subscribe(mobile_app, "weather")
    weather_station.subscribe(web_interface, "weather")
    weather_station.subscribe(desktop_app, "weather")

    # Simulate weather data update
    weather_station.publish("weather", "Temperature: 32.5, Humidity: 50.0, Pressure: 983.15")


if __name__ == "__main__":
    main()
