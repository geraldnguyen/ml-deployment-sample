import numpy as np

from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the exported model
exported_model_filename = 'random_model.joblib'
model = joblib.load(exported_model_filename)

# API endpoint for model prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)[0]
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
