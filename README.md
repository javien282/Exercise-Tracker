# Exercise Tracker Application

This Exercise Tracker application allows users to log their daily workouts, track calories burned, and store the data securely in a Google Sheet. The application integrates with the Nutritionix API to analyze exercise data based on user input and utilizes the Sheety API to automate data logging.

## Features

- **Real-Time Exercise Tracking**: Input your workout activities, and the app calculates the duration and calories burned.
- **API Integration**: Utilizes Nutritionix API for exercise data analysis and Sheety API for storing workout data.
- **Secure Authentication**: API keys and user credentials are securely managed using environment variables.
- **Automated Data Logging**: Automatically records exercise details, including date, time, activity type, duration, and calories burned, in a Google Sheet.

## Technologies Used

- **Python**: Core programming language.
- **Requests**: Python library used to handle HTTP requests.
- **Nutritionix API**: For exercise data analysis.
- **Sheety API**: To log exercise data in a Google Sheet.
- **HTTP Basic Authentication**: For secure communication with the Sheety API.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/exercise-tracker.git
   cd exercise-tracker

2. Install required Dependances
   pip install -r requirements.txt

3. Set up environment variables for API keys and authentication:
   export APP_ID="your_nutritionix_app_id"
   export API_KEY="your_nutritionix_api_key"
   export USERNAME="your_sheety_username"
   export PASSWORD="your_sheety_password"
   export SHEET_ENDPOINT="your_sheety_endpoint"


5. Run the application:
  python main.py

## Usage

1.	Upon running the application, input the exercises you performed when prompted.
2.	The application will send the exercise data to the Nutritionix API to calculate the duration and calories burned.
3.	The results will be automatically logged into your Google Sheet via the Sheety API.

## Example

What exercises did you do today?
> Ran 5km and did 30 minutes of yoga

Logging data...
Data logged successfully:
- Ran: 30 minutes, 300 calories
- Yoga: 30 minutes, 200 calories

## Project Structure 

.
├── main.py            # Main application script
├── requirements.txt   # List of dependencies
└── README.md          # Project documentation

