from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        locality = request.form['locality']
        
        if not locality:
            return jsonify({"error": "Locality name cannot be empty"}), 400  # Bad Request
        
        # Call your ML model's prediction function here
        predicted_power = fake_ml_model(locality)  # Placeholder for actual ML function
        
        return jsonify({"locality": locality, "predicted_power": predicted_power})

    except Exception as e:
        # Generic server error
        return jsonify({"error": "An error occurred processing your request"}), 500

# Placeholder model function
def fake_ml_model(locality):
    return 500  # Example value, replace with actual model output

# Custom error handlers
@app.errorhandler(400)
def bad_request_error(e):
    return render_template('error.html', error_code=400, error_message="Bad Request: Please check your input and try again."), 400

@app.errorhandler(404)
def not_found_error(e):
    return render_template('error.html', error_code=404, error_message="Page Not Found: The page you are looking for does not exist."), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error_code=500, error_message="Internal Server Error: Something went wrong on our end."), 500

if __name__ == "__main__":
    app.run(debug=True)
