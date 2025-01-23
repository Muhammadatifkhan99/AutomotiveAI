#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <nlohmann/json.hpp>

// For convenience
using json = nlohmann::json;

// Function to calculate the Euclidean distance between two points
double euclidean_distance(const std::vector<double>& p1, const std::vector<double>& p2) {
    double sum = 0.0;
    for (size_t i = 0; i < p1.size(); ++i) {
        sum += (p1[i] - p2[i]) * (p1[i] - p2[i]);
    }
    return std::sqrt(sum);
}

// Function to calculate the Lane Marking Accuracy
double calculate_lma(const json& data) {
    double total_error = 0.0;
    for (const auto& sample : data) {
        const auto& predicted = sample["predicted"].get<std::vector<double>>();
        const auto& ground_truth = sample["ground_truth"].get<std::vector<double>>();
        total_error += euclidean_distance(predicted, ground_truth);
    }
    return total_error / data.size();
}

int main() {
    // Read JSON file
    std::ifstream file("lane_marking_data.json");
    if (!file.is_open()) {
        std::cerr << "Failed to open file" << std::endl;
        return 1;
    }

    json data;
    file >> data;

    // Calculate Lane Marking Accuracy
    double lma = calculate_lma(data);
    std::cout << "Lane Marking Accuracy: " << lma << std::endl;

    return 0;
}