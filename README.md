# WeatherApp

A very simple desktop weather application built with Python and PyQt5.

This is a basic starter project that someone could use as a foundation for building their own weather application without having to write all the basic code from scratch.

Keep in mind that I'm new to coding, and this is my first real project. I'm still learning, so I hope to make it much better as I gain more experience!

## Features
- City search
- Temperature in Celsius
- Local time and day/night status
- Weather conditions
- Wind speed and direction
- Humidity and UV index

## Requirements
- Python
- Requests
- PyQt5

## Installation
```bash
pip install -r requirements.txt
```

## API Key Setup

This project uses [WeatherAPI](https://www.weatherapi.com/) to retrieve weather information.

To use the application:

1. Create a free account at [WeatherAPI.com](https://www.weatherapi.com/signup).
2. Get your personal API key from your dashboard.
3. Set an environment variable named `WEATHER_API_KEY` containing your API key.

### Windows (PowerShell)
```powershell
$env:WEATHER_API_KEY="YOUR_API_KEY"
```

### Linux (Terminal)
```bash
export WEATHER_API_KEY="YOUR_API_KEY"
```

### macOS (Terminal)
```bash
export WEATHER_API_KEY="YOUR_API_KEY"
```

**Note:** You need your own API key to run the application. The environment variable must be set each time you open a new terminal session. Do not share your API key publicly.

## Usage
```bash
python main.py
```

## Known Limitations
- Error handling is not fully implemented yet.
- Requires an internet connection and a valid WeatherAPI key.
