from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_data():
    # POST request
    pass

@app.route('/retrieve', methods=['GET'])
def retrieve_data():
    # GET request
    pass

if __name__ == '__main__':
    app.run(debug=True)
