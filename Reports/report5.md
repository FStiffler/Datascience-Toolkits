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
