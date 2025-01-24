import requests
import random
from datetime import datetime, timezone
import time

# Base URL for the Flask API running on localhost
BASE_URL = "http://127.0.0.1:5000"

def generate_random_gps_data():
    """
    Generate a random GPS data point with a timestamp, latitude, and longitude.
    """
    timestamp = datetime.now(timezone.utc).isoformat() + "Z"  # Corrected datetime formatting
    latitude = round(random.uniform(-90, 90), 4)
    longitude = round(random.uniform(-180, 180), 4)
    return {
        "timestamp": timestamp,
        "latitude": latitude,
        "longitude": longitude
    }

def send_post_request():
    """
    Send a POST request with random GPS data to the '/upload' endpoint.
    """
    url = f"{BASE_URL}/upload"
    gps_data = generate_random_gps_data()

    try:
        response = requests.post(url, json=gps_data, timeout=5)
        if response.status_code == 200:
            print("POST Request Success: ", response.json())
        else:
            print("POST Request Failed. Status Code:", response.status_code)
            print("Response Text:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error during POST request: {e}")

def send_get_request():
    """
    Send a GET request to the '/retrieve' endpoint to fetch processed data.
    """
    url = f"{BASE_URL}/retrieve"

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("GET Request Success: ", response.json())
        else:
            print("GET Request Failed. Status Code:", response.status_code)
            print("Response Text:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error during GET request: {e}")

if __name__ == "__main__":
    print("Starting API Tester...")

    try:
        while True:
            print("\nSending POST request...")
            send_post_request()

            time.sleep(1)

            print("\nSending GET request...")
            send_get_request()

            time.sleep(2)
    except KeyboardInterrupt:
        print("\nAPI Tester stopped by user.")
