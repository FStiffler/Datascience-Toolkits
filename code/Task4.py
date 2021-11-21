# laying out the basis from previous tasks and/or Milestones

import psycopg2
import numpy as np
from tensorflow import keras
import pickle
from PIL import Image
import os

# connect to postgres db initalised by docker compose
con = psycopg2.connect(
    host="db",
    port="5432",
    database="postgres",
    user="admin",
    password="1234")

# Turn off transaction mode and enable autocommit
con.autocommit = True

# Creat cursor
cur = con.cursor()

# Create new database 'milestone_3' if not existing y_test
cur.execute('SELECT datname FROM pg_database;')
db_list = cur.fetchall()

if ('milestone_3',) not in db_list:

    # create database milestone
    cur.execute('CREATE DATABASE milestone_3')

# Close connection
con.close()

# connect to postgres db initalised by docker compose
con = psycopg2.connect(
    host="db",
    port="5432",
    database="milestone_3",
    user="admin",
    password="1234")

# Turn off transaction mode and enable autocommit
con.autocommit = True

# Creat cursor
cur = con.cursor()

# creating the input data table
cur.execute('''
    CREATE TABLE input_data (
    InputID int PRIMARY KEY
        GENERATED ALWAYS AS IDENTITY,
    Picture bytea,
    Label int);
    ''')

# creating the predictions table
cur.execute('''
    CREATE TABLE predictions (
    PredictionID int PRIMARY KEY
        GENERATED ALWAYS AS IDENTITY,
    InputID int
        REFERENCES input_data(InputID),
    prediction int);
    ''')

# import already existing module
from data_load import load_data

# load data
x_train, y_train, x_test, y_test = load_data()

# take first picture of training data as sample
sample = x_train[0]
sample_label = int(y_train[0])

# Visualize picture
Image.fromarray(sample).show()

# Transform picture to byte stream
sample_bytes = pickle.dumps(sample)

# Insert picture to input table
cur.execute(
    """
    INSERT INTO input_data (Picture, Label)
    VALUES (%s, %s)
    """,
    (sample_bytes, sample_label))

# Select transformed sample from input table and store it as python object
cur.execute('SELECT Picture FROM input_data')
sample_bytes_loaded = cur.fetchone()[0]

# Select transformed sample from input table and store it as python object
cur.execute('SELECT InputID FROM input_data')
sample_ID = int(cur.fetchone()[0])

# Retransform to object
sample_back = pickle.loads(sample_bytes_loaded)

# Visualize picture
Image.fromarray(sample_back).show()

# import model
model_name = "mnist_convnet_model.h5"  # how the model shall be named
model_save_dir = os.path.join(os.getcwd(), 'saved_models')  # relative path to save models in
from handling_model import load_model
model = load_model(model_save_dir, model_name)

# transform data to be predicted
sample_back = sample_back.astype("float32") / 255
sample_back = np.expand_dims(sample_back, -1)
sample_back_final = np.array([sample_back])  # Model expects shape (x, 28, 28, 1)

# make predictions
predictions = model.predict(sample_back_final)

# final prediction
final_pred = int(np.argmax(predictions[0]))

# Insert predictions into table
cur.execute(
    """
    INSERT INTO predictions (InputID, prediction)
    VALUES (%s, %s)
    """,
    (sample_ID, final_pred))
