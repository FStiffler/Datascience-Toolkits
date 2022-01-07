import flask

app  = Flask(__name__)

@app.route('/')
def welcome():

    return 'Welcome to this app' 
