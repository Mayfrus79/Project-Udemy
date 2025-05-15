import sys
import requests
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class Locator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IP and Location Finder")

        # Layout
        layout = QVBoxLayout()

        # Button
        self.button = QPushButton("Get Location")
        self.button.clicked.connect(self.get_location)

        # Labels to display information
        self.label_ip = QLabel("IP: ")
        self.label_location = QLabel("Location: ")

        # Add widgets to layout
        layout.addWidget(self.button)
        layout.addWidget(self.label_ip)
        layout.addWidget(self.label_location)

        self.setLayout(layout)

    def get_location(self):
        try:
            # Get IP and location using API
            response = requests.get("https://ipinfo.io/json")
            data = response.json()

            ip = data.get("ip", "Unknown")
            city = data.get("city", "")
            region = data.get("region", "")
            country = data.get("country", "")
            loc = data.get("loc", "")  # Latitude and longitude

            self.label_ip.setText(f"IP: {ip}")
            self.label_location.setText(f"Location: {city}, {region}, {country} ({loc})")
        except Exception as e:
            self.label_ip.setText("Error retrieving IP")
            self.label_location.setText(str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Locator()
    window.show()
    sys.exit(app.exec())
