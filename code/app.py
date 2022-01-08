from flask import Flask, jsonify, request
import os
import numpy as np
from handling_model import load_model
from db import create_table, save_predictions

# Variables
model_name = "mnist_convnet_model.h5"  # how the model shall be named
model_save_dir = os.path.join(os.getcwd(), 'saved_models')  # relative path to save models in

# Check if model already exists
if os.path.isfile(os.path.join(model_save_dir,model_name)):

    # Load model
    model = load_model(model_save_dir, model_name)

else:

    # Train model
    import main

    # Load model
    model = load_model(model_save_dir, model_name)


# Create tables in sql database only if it does not already exist
try:
    create_table()
except Exception:
    pass

app  = Flask(__name__)

@app.route('/', methods=['GET'])
def get_information():
    return "<h1>Welcome!</h1><br>Send a POST request to '/predict' with your MNIST picture to receive a prediction"


@app.route('/predict', methods=['POST'])
def get_prediction():

    # Get input and prepare
    input = request.get_json(force=True)
    input_image = np.array(input['image'])
    image = input_image.astype("float32") / 255
    image = np.expand_dims(image, -1)
    image = np.array([image])  # Model expects shape (x, 28, 28, 1)

    # make predictions
    predictions = model.predict(image)

    # final prediction
    final_pred = int(np.argmax(predictions[0]))

    # save predictions in database
    save_predictions(input_image, final_pred)

    # dictionary with prediction
    user_return = {'prediction':final_pred}

    return jsonify(user_return)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
