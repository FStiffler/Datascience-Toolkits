# laying out the basis from previous tasks and/or Milestones

import psycopg2
import numpy as np
from tensorflow import keras
import pickle
from PIL import Image

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
db_list = cur.execute('SELECT datname FROM pg_database;')

if 'milestone_3' not in db_list:
    cur.execute('CREATE DATABASE milestone_3')

# Close connection
con.close()

# creating the input data table
cur.execute('''
    CREATE TABLE input_data (
    Input_ID int PRIMARY KEY
        GENERATED ALWAYS AS IDENTITY,
    Picture bytea,
    Label int);
    ''')

# creating the predictions table
cur.execute('''
    CREATE TABLE predictions (
    Prediction_ID int PRIMARY KEY
        GENERATED ALWAYS AS IDENTITY,
    Input_ID int
        REFERENCES input_data(Input_ID)
    prediction int);
    ''')

# import already existing module
from data_load import load_data


# Load and store the sample image from data

# [1]
# load data
x_train, y_train, x_test, y_test = load_data()

# take first picture of training data as sample
sample = x_train[0]

# Visualize picture
Image.fromarray(sample).show()

# Transform picture to byte stream
sample_bytes = pickle.dumps(sample)

cur = con.cursor()
cur.execute(
    """
    INSERT INTO input_data (Picture)
    VALUES (%s)
    """,
    (sample_bytes, ))

# [2]
# take first picture of training data as sample
sample = x_train[0]

# Visualize picture
Image.fromarray(sample).show()

# Transform picture to byte stream
sample_bytes = pickle.dumps(sample)

cur = con.cursor()
cur.execute(
    """
    INSERT INTO predictions (Picture)
    VALUES (%s)
    """,
    (sample_bytes, ))

# executing query
cur.execute("select * from input_data;")
print("The sample input tested:")
print(cur.fetchall())


cur.execute("select * from predictions;")
print("The produced prediction from the tested sample:")
print(cur.fetchall())


# commit data to db
con.commit()


con.close()
