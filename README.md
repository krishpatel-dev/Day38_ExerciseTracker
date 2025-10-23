# 🐍 Exercise Tracker - Day 38

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/krishpatel-dev/BasicPy4/graphs/commit-activity)

Welcome to the Exercise Tracker project! 🚀 This Python application helps you track your workouts by connecting to the Nutritionix API to get exercise data and storing it in a Google Sheet using Sheety.

## 📋 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Setup](#-setup)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Contributing](#-contributing)

## ✨ Features

- 🏃 Track various exercises with natural language input
- 📊 Automatically calculates calories burned
- 📅 Logs date and time of each workout
- 📊 Stores data in Google Sheets for easy tracking
- 🔒 Secure authentication for API access

## 📋 Prerequisites

- Python 3.8 or higher
- Nutritionix API key
- Sheety API access
- Google account (for Google Sheets)

## 🛠 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/krishpatel-dev/Day38_exercise_tracker.git
   cd Day38_exercise_tracker
   ```

2. **Install required packages**
   ```bash
   pip install requests python-dotenv
   ```

## ⚙️ Configuration

1. Sign up for a [Nutritionix API](https://www.nutritionix.com/business/api) account to get your API credentials
2. Create a new Google Sheet and set up [Sheety](https://sheety.co/) to connect to it
3. Create a `.env` file in the project root and add your credentials:
   ```
   NUTRITIONIX_APP_ID=your_app_id_here
   NUTRITIONIX_API_KEY=your_api_key_here
   SHEETY_USERNAME=your_sheety_username
   SHEETY_PASSWORD=your_sheety_password
   SHEET_ENDPOINT=your_sheety_endpoint_url
   ```

## 🚀 Usage

1. Update the following variables in `Proj38_exercise_tracker.py` with your personal information:
   ```python
   GENDER = "male"  # or "female"
   WEIGHT_KG = 84   # your weight in kg
   HEIGHT_CM = 180  # your height in cm
   AGE = 32         # your age
   ```

2. Run the script:
   ```bash
   python Proj38_exercise_tracker.py
   ```

3. Enter your exercise in natural language when prompted, for example:
   - "ran 5 km in 30 minutes"
   - "swam 20 minutes"
   - "cycled 10 km in 25 minutes"

## 🧠 How It Works

1. The script takes natural language input about your exercise
2. It sends this data to the Nutritionix API to get exercise details
3. The response includes calories burned and other metrics
4. This data is then sent to your Google Sheet via the Sheety API
5. Your workout is logged with date, time, exercise details, and calories burned

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

<div align="center">
  Made with ❤️ and ☕ by <b>Krish</b>
</div>
