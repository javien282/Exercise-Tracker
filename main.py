import os
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

GENDER = "Female"
WEIGHT_KG = "58"
HEIGHT_CM = "142.72"
AGE = "30"

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

NUTRITIONIX_HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

basic = HTTPBasicAuth(username=USERNAME, password=PASSWORD)

workout = input("What exercises did you do today?\n")

nutrititonix_params = {
    "query": workout,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_ENDPOINT,
                         headers=NUTRITIONIX_HEADER,
                         json=nutrititonix_params)
result = response.json()

today_date = datetime.now().strftime("%m/%d/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_params = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT,
                                   auth=basic,
                                   json=sheet_params)
    sheet_result = sheet_response.text
