import random
import time
from datetime import datetime

# Function to generate random GPS data
def generate_random_gps_data():
    # Get the current timestamp in ISO 8601 format (UTC)
    timestamp = datetime.utcnow().isoformat() + "Z"

    # Generate a random latitude between -90 and 90
    latitude = round(random.uniform(-90, 90), 4)

    # Generate a random longitude between -180 and 180
    longitude = round(random.uniform(-180, 180), 4)

    # Create the data in the required JSON-like structure
    gps_data = {
        "timestamp": timestamp,
        "latitude": latitude,
        "longitude": longitude
    }

    return gps_data

# Simulate real-time data generation every 2 seconds
def simulate_data_generation():
    while True:
        # Generate random GPS data
        gps_data = generate_random_gps_data()

        # Print the generated data (or it can be sent to a database or API)
        print(gps_data)

        # Wait for 2 seconds before generating the next data point
        time.sleep(2)

# Call the function to start the simulation
simulate_data_generation()
