import json
import random
import math

# Generate random data for lane markings
def generate_random_data(num_samples):
    data = []
    for _ in range(num_samples):
        sample = {
            "predicted": [random.uniform(0, 1000) for _ in range(4)],  # 4 points for a lane
            "ground_truth": [random.uniform(0, 1000) for _ in range(4)]  # 4 points for a lane
        }
        data.append(sample)
    return data

# Save data to JSON file
def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Generate and save data
num_samples = 1000
data = generate_random_data(num_samples)
save_to_json(data, 'lane_marking_data.json')


# Function to calculate the Euclidean distance between two points
def euclidean_distance(predicted_point, ground_truth_point):
    """
    Calculate the Euclidean distance between two points.

    :param predicted_point: List of coordinates for the predicted point
    :param ground_truth_point: List of coordinates for the ground truth point
    :return: Euclidean distance between the two points
    """
    sum_of_squares = 0.0  # Initialize the sum of squared differences
    for i in range(len(predicted_point)):
        # Calculate the square of the difference for each coordinate
        sum_of_squares += (predicted_point[i] - ground_truth_point[i]) ** 2
    # Return the square root of the sum of squares
    return math.sqrt(sum_of_squares)

# Function to calculate the Lane Marking Accuracy
def calculate_lma(data):
    #Calculate the Lane Marking Accuracy (LMA) by averaging the Euclidean distances between predicted and ground truth points.
    #:param data: List of dictionaries containing predicted and ground truth points
    #:return: Lane Marking Accuracy (LMA)
    total_error = 0.0  # Initialize the total error to zero
    for sample in data:
        # Extract the predicted and ground truth points from the sample
        predicted = sample["predicted"]
        ground_truth = sample["ground_truth"]
        # Calculate the Euclidean distance between the predicted and ground truth points
        error = euclidean_distance(predicted, ground_truth)
        # Add the error to the total error
        total_error += error
    # Calculate the average error (LMA) by dividing the total error by the number of samples
    lma = total_error / len(data)
    return lma

# Main function to read the JSON file and calculate the LMA
def main():
    # Open the JSON file for reading
    with open('lane_marking_data.json', 'r') as file:
        # Load the JSON data from the file
        data = json.load(file)

    # Calculate the Lane Marking Accuracy
    lma = calculate_lma(data)

    # Print the Lane Marking Accuracy
    print("Lane Marking Accuracy: ", lma)

# Entry point of the script
if __name__ == "__main__":
    main()
