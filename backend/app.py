# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # Enable CORS to allow cross-origin requests

# Define a route for calorie estimation
@app.route('/api/estimate_calories', methods=['POST'])
def estimate_calories():
    # Implement the calorie estimation logic here
    # You'll need to process the uploaded image and use your CNN model

    # For demo purposes, let's return a dummy response
    result = {
        'estimated_calories': 200
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)