import requests
import random
from datetime import datetime
import time

# Base URL for the Flask API running on localhost
BASE_URL = "http://127.0.0.1:5000"

# Function to generate random GPS data
def generate_random_gps_data():
    """
    Generate a random GPS data point with a timestamp, latitude, and longitude.
    """
    timestamp = datetime.datetime.now(timezone.utc).isoformat() + "Z"
    latitude = round(random.uniform(-90, 90), 4)
    longitude = round(random.uniform(-180, 180), 4)
    return {
        "timestamp": timestamp,
        "latitude": latitude,
        "longitude": longitude
    }

# Function to send a POST request to the API
def send_post_request():
    """
    Send a POST request with random GPS data to the '/upload' endpoint.
    """
    url = f"{BASE_URL}/upload"
    gps_data = generate_random_gps_data()

    try:
        response = requests.post(url, json=gps_data)
        if response.status_code == 200:
            print("POST Request Success: ", response.json())
        else:
            print("POST Request Failed: ", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error during POST request: {e}")

# Function to send a GET request to the API
def send_get_request():
    """
    Send a GET request to the '/retrieve' endpoint to fetch processed data.
    """
    url = f"{BASE_URL}/retrieve"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("GET Request Success: ", response.json())
        else:
            print("GET Request Failed: ", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error during GET request: {e}")

# Main function to test the API
if __name__ == "__main__":
    print("Starting API Tester...")

    # Loop to continuously test the API
    try:
        while True:
            # Send a POST request with random data
            print("\nSending POST request...")
            send_post_request()

            # Wait for a second before sending a GET request
            time.sleep(1)

            # Send a GET request to fetch processed data
            print("\nSending GET request...")
            send_get_request()

            # Wait for 2 seconds before repeating
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nAPI Tester stopped by user.")
