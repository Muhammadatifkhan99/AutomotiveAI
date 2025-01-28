from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = []  # In-memory storage for GPS data

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid data"}), 400
    data_store.append(data)
    return jsonify({"message": "Data received", "data": data}), 200

@app.route('/retrieve', methods=['GET'])
def retrieve():
    return jsonify({"data": data_store}), 200

if __name__ == "__main__":
    app.run(debug=True)  # Default runs on http://127.0.0.1:5000
