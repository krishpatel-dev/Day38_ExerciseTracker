import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 180
AGE = 32

APP_ID = ""
API_KEY = ""
USERNAME = ""
PASSWORD = ""

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/45e9136f2c27586e7b04f8df9b2fbc77/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

# Nutritionix API Call
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #No Authentication
    # sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)
    #
    # print(sheet_response.text)

    sheet_response = requests.post(
        url=sheet_endpoint,
        json=sheet_inputs,
        auth=(
            USERNAME,
            PASSWORD,
        )
    )

    print(sheet_response.text)
