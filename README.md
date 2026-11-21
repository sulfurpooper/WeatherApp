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
- A WeatherAPI key

## Setup

Download the repository using **Code → Download ZIP** and extract it, or clone it using Git.

Open a terminal in the project folder and install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## API Key Setup

This project uses [WeatherAPI](https://www.weatherapi.com/) to retrieve weather information.

Create a free account at [WeatherAPI.com](https://www.weatherapi.com/signup) and get your API key.

Set an environment variable named `WEATHER_API_KEY`, replacing `YOUR_API_KEY` with your actual key:

**Windows (Command Prompt / CMD):**
```cmd
set WEATHER_API_KEY=YOUR_API_KEY
```

**Windows (PowerShell):**
```powershell
$env:WEATHER_API_KEY="YOUR_API_KEY"
```

**Linux / macOS:**
```bash
export WEATHER_API_KEY="YOUR_API_KEY"
```

## Usage

Run the application from the same terminal:

```bash
python main.py
```

If `python` doesn't work, try `python3`.

**Note:** The API key must be set again whenever you open a new terminal session.

## Known Limitations
- Error handling is not fully implemented yet.
- Requires an internet connection and a valid WeatherAPI key.
