import json
import random

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
