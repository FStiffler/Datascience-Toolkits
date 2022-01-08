# Report: Milestone 5         

## Task 1

The first task was to follow this [tutorial](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-o n-ubuntu-18-04) to learn more about flask. So we did that.

We had to made sure to install Nginx as described in step one [here](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04) because it is a requirement to get flask running.

After we read through the tutorial, we decided to apply the learnings right away in task 2.

## Task 2

**1. Expose a REST endpoint**

Our python files which we used so far are stored in the directory `code` and are referencing each other to accomplish tasks demanded in previous milestones. For this reason we decided to add an `app.py` file to the same directory to build our flask application. We started out by just trying to get a app running, exposing a REST endpoint which prints a welcome message to the user. But we really struggled to understand what to do so we decided to take a step back and look at another [tutorial](https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/). To understand the whole ideas of endpoints a bit better we additionally visited this [page](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/). Finally getting the basic idea of flask, we were able to create code which showed a welcome message to the user when the defined `welcome` endpoint was called via localhost:

`http://localhost:<port>/welcome`

The port is 5000 by default. We did not define it manually but when we run the file in the console we got notified that app is running on this port.

**2. Accepting a POST request**

The next step was to send a post request to the web app and get a response back in return. For this purpose we installed the `request` library into our virtual environments. After that we created a temporary python file to create and send requests in order to test the endpoints. Again we consulted a online [article](https://www.nylas.com/blog/use-python-requests-module-rest-apis/) to do so. We decided to do some arbitrary test request first to learn the basics. For that purpose we used the income example of the [second source](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/) provided before. We created a flask app capable of handling GET and POST requests. Then we sent requests to the application with the goal to append a new income figure to a list of incomes and return the list. Here the code to send requests:

```
import requests

response = requests.get("http://localhost:5000/incomes")
print(response.json())

response = requests.post("http://localhost:5000/incomes", json = {"description": "lottery","amount": 1000.0})
print(response.json())
```

It sends a GET request first and a POST request second and prints the response in either cases.
The requests are handled by the application:

```
from flask import Flask, jsonify, request

app  = Flask(__name__)

incomes = [
  { 'description': 'salary', 'amount': 5000 }
]


@app.route('/incomes', methods=['GET'])
def get_incomes():
    return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_incomes():
    incomes.append(request.get_json())
    return jsonify(incomes)


if __name__ == "__main__":
    app.run(debug=True)

```

The application simply returns the income dictionary in case of the GET request and appends the new income entry in the case of the POST request and then returns the appended dictionary in json format. Now that we had a deeper understanding of how to handle POST requests, we wanted to make a step forward and create requests with a whole picture in the body.

**3. POST request with image in body**

To send a whole image in the body of a request we had to adjust our request file. First of all we used the modules we created in an earlier milestone to load the MNIST data. After that we selected a random image. The image is transformed so that it can be sent with a POST request to our application:

```
import requests
import json

# Load data
from data_load import load_data
x_train, y_train, x_test, y_test = load_data()

# Select first image of test data and convert to list
image = x_test[0].tolist()

# Transform input to dictionary
requestDict = {'image':image}


response = requests.post("http://localhost:5000/predict", json=requestDict)
print(response.json())

```

**4. Return prediction and store results in DB**

First we wanted just to be able to return the prediction result. For that we had to modify our `app.py` file. We were not sure what the best way was to use the existing modules. But we decided that we would run `main.py` again with the parameters defined in the last milestone and train a new model. This model was stored in the directory `code/saved_models`. Instead of running the main file everytime we start the app new, we decided to just load the model from this directory. But this also means we have to make sure the model is also copied to the container later on. We had some struggles with the requests because it seemed that the incoming request was not correctly identified as a JSON format. But after some time we figured our the problem and were successfully able to return the return the prediction to the user. Up to this point our application file looked like this:

```
from flask import Flask, jsonify, request
import os
import numpy as np
from handling_model import load_model

# Variables
model_name = "mnist_convnet_model.h5"  # how the model shall be named
model_save_dir = os.path.join(os.getcwd(), 'saved_models')  # relative path to save models in

# Load model
model = load_model(model_save_dir, model_name)

app  = Flask(__name__)

@app.route('/', methods=['GET'])
def get_information():
    return "<h1>Welcome!</h1><br>Send a POST request to '/predict' with your MNIST picture to receive a prediction"


@app.route('/predict', methods=['POST'])
def get_prediction():

    # Get input and prepare
    input = request.get_json(force=True)
    image = np.array(input['image'])
    image = image.astype("float32") / 255
    image = np.expand_dims(image, -1)
    image = np.array([image])  # Model expects shape (x, 28, 28, 1)

    # make predictions
    predictions = model.predict(image)

    # final prediction
    final_pred = int(np.argmax(predictions[0]))

    # dictionary with prediction
    user_return = {'prediction':final_pred}

    return jsonify(user_return)


if __name__ == "__main__":
    app.run(debug=True)

```

The next step was to make sure that the user inputs and the predictons are stored in the data base. For that we went back to the file we used for milestone 3 to store our results in a data base. We created a new file `db.py` which would contain functions to store the image and the prediction in a defined database. This file has two functions. One to create a new table to store the predictions and one to store actual values in the table. The file looks as follows:

```
import psycopg2
import pickle


def create_table():

    # connect to postgres db initalised by docker compose
    con = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="admin",
        password="1234")

    # Turn off transaction mode and enable autocommit
    con.autocommit = True

    # Creat cursor
    cur = con.cursor()

    # creating table to save image and prediction
    cur.execute('''
        CREATE TABLE predictions (
        PredictionID int PRIMARY KEY
            GENERATED ALWAYS AS IDENTITY,
        Picture bytea,
        Prediction int);
        ''')

    # Close connection
    con.close()

def save_predictions(input_image, prediction):

    # connect to postgres db initalised by docker compose
    con = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="admin",
        password="1234")

    # Turn off transaction mode and enable autocommit
    con.autocommit = True

    # Create cursor
    cur = con.cursor()

    # Transform picture to byte stream
    sample_bytes = pickle.dumps(input_image)

    # Insert picture to input table
    cur.execute(
        """
        INSERT INTO predictions (Picture, Prediction)
        VALUES (%s, %s)
        """,
        (sample_bytes, prediction))

    # Close connection
    con.close()

```

To test if the functions really worked we ran a docker container with pgAdmin and PostgresSQL on our localhost. After several tries the functions worked fine. But now we had to implement them into our app. This proved to be harder then expected. We had some issues because running the application would throw an error because the SQL table to be created was already there when the app was initiated, shut down and initiated again. So we had to define an exception for this case. Also we called the second db function with wrong arguments a few times before it worked. Challenging was also to really understand what happens with the image in the POST request and how we need to define ports and dependencies to get everything working. But eventually we were able to handle it. The final application looked like this:

```
from flask import Flask, jsonify, request
import os
import numpy as np
from handling_model import load_model
from db import create_table, save_predictions

# Variables
model_name = "mnist_convnet_model.h5"  # how the model shall be named
model_save_dir = os.path.join(os.getcwd(), 'saved_models')  # relative path to save models in

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
    app.run(debug=True)


```

As you can see, the application first imports all necessary libraries and modules, loads the model, creates database tables if they are not there yet and then creates two endpoints. The first endpoint contains information about how to send a request. The second endpoint receives a POST request with a picture, makes a prediction, stores the picture and the prediction in a database and returns the prediction to the user. 
