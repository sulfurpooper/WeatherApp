import sys
import requests 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_name = QLabel("Enter City Name", self)
        self.city_input = QLineEdit(self)
        self.weather_button = QPushButton("Get Weather", self)
        self.temp_label = QLabel(self)
        self.describe_label = QLabel(self)
        self.time_label = QLabel(self)
        self.data = None
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setFixedSize(500, 600)
        vbox = QVBoxLayout()

        vbox.addWidget(self.city_name)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.describe_label)
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.city_name.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.describe_label.setAlignment(Qt.AlignCenter)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setObjectName("time_label")
        self.city_name.setObjectName("city_name")
        self.city_input.setObjectName("city_input")
        self.weather_button.setObjectName("weather_button")
        self.temp_label.setObjectName("temp_label")
        self.describe_label.setObjectName("describe_label")

        self.setStyleSheet("""
        QLabel{
        font-family: Arial;
        font-size: 30px;
        }
        QLineEdit{
        font-family: Arial;
        font-size: 30px;
        padding: 15px;
        }
        QPushButton{
        font-family: Arial;
        font-size: 30px;
        }
        """)

        self.weather_button.clicked.connect(self.get_weather)
        self.weather_button.clicked.connect(self.describe_weather)

    def get_weather(self):
        city = self.city_input.text().capitalize().strip()
        request = requests.get(f"https://api.weatherapi.com/v1/forecast.json?key=YOUR_API_KEY_HERE&q={city}&days=3&aqi=no&alerts=yes")
        self.data = request.json()
        tempeture = self.data["current"]["temp_c"]
        self.temp_label.setText(str(f"{tempeture}°C"))

    def describe_weather(self):
        local_time = self.data["location"]["localtime"]
        hour_minute = local_time[11:16]
        city = self.data["location"]["name"]
        is_day = self.data["current"]["is_day"]
        if is_day == 1:
            day_night = "Day"
        else:
            day_night = "Night"
        country = self.data["location"]["country"]
        humidity = self.data["current"]["humidity"]
        uv = self.data["current"]["uv"]
        condition = self.data["current"]["condition"]["text"]
        wind = self.data["current"]["wind_kph"]
        direction = self.data["current"]["wind_dir"]
        
        self.describe_label.setText(f"{city}/{country}\n{hour_minute} {day_night}\n{condition}\nWind Speed: {wind}\nWind Direction: {direction}\nHumidity: {humidity}%\nUV: {uv}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
