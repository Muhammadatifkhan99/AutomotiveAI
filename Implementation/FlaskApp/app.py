import json
import random
import time
from datetime import datetime
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Define file paths for storing incoming and processed data
INCOMING_DATA_FILE = "incoming_data.json"
PROCESSED_DATA_FILE = "processed_coordinates.json"

# Function to generate random GPS data
def generate_random_gps_data():
    timestamp = datetime.utcnow().isoformat() + "Z"
    latitude = round(random.uniform(-90, 90), 4)
    longitude = round(random.uniform(-180, 180), 4)
    return {
        "timestamp": timestamp,
        "latitude": latitude,
        "longitude": longitude
    }

# Function to save data to a file (append mode)
def save_to_file(file_name, data):
    try:
        with open(file_name, "a") as file:
            json.dump(data, file)
            file.write("\n")
    except Exception as e:
        print(f"Error saving data to {file_name}: {e}")

# Function to process incoming GPS data (calculate average latitude and longitude)
def process_data():
    try:
        with open(INCOMING_DATA_FILE, "r") as file:
            data_points = [json.loads(line) for line in file.readlines()]
        
        # If no data is available, return an empty summary
        if not data_points:
            return {"average_latitude": 0, "average_longitude": 0}

        # Calculate the average latitude and longitude
        total_latitude = sum([point['latitude'] for point in data_points])
        total_longitude = sum([point['longitude'] for point in data_points])
        avg_latitude = total_latitude / len(data_points)
        avg_longitude = total_longitude / len(data_points)

        # Prepare processed data
        processed_data = {
            "average_latitude": round(avg_latitude, 4),
            "average_longitude": round(avg_longitude, 4)
        }

        # Save the processed data to a file
        save_to_file(PROCESSED_DATA_FILE, processed_data)
        return processed_data
    except Exception as e:
        print(f"Error processing data: {e}")
        return {}

# POST endpoint to receive and store incoming GPS data
@app.route('/upload', methods=['POST'])
def upload_data():
    try:
        # Get the incoming data from the request
        incoming_data = request.get_json()

        # Save the incoming data to the incoming data file
        save_to_file(INCOMING_DATA_FILE, incoming_data)

        # Return a success message
        return jsonify({"message": "Data received and stored successfully!"}), 200
    except Exception as e:
        print(f"Error in uploading data: {e}")
        return jsonify({"error": "Failed to store data"}), 400

# GET endpoint to retrieve processed GPS data
@app.route('/retrieve', methods=['GET'])
def retrieve_processed_data():
    try:
        # Process the incoming data and calculate summary
        processed_data = process_data()

        # Return the processed data
        return jsonify(processed_data), 200
    except Exception as e:
        print(f"Error in retrieving processed data: {e}")
        return jsonify({"error": "Failed to retrieve processed data"}), 400

# Function to simulate real-time data generation and send POST requests
def simulate_data_generation():
    while True:
        # Generate random GPS data
        gps_data = generate_random_gps_data()

        # Simulate sending POST request with generated GPS data to the backend
        with app.test_client() as client:
            client.post('/upload', json=gps_data)

        # Wait for 2 seconds before generating the next data point
        time.sleep(2)

# Start server
if __name__ == '__main__':
    # Start the app
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)

    # data generation
    simulate_data_generation()

#to send a post request use:::    curl -X POST http://<ngrok_url>/upload -H "Content-Type: application/json" -d '{"timestamp":"2025-01-23T12:00:00Z","latitude":52.5200,"longitude":13.4050}'
#to send a get request use:::     curl http://127.0.0.1:5000/retrieve

