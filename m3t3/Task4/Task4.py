# laying out the basis from previous tasks and/or Milestones

host = "localhost"
database = "milestone_3"
port = "5432"
user = "admin"
password = "1234"

import psycopg2
import numpy as np

con = psycopg2.connect(
    host="localhost",
    port="5432",
    database="milestone_3",
    user="admin",
    password="1234")

cur = con.cursor()

# creating the input data table
cur.execute('''
    CREATE TABLE input_data (
    ID SERIAL PRIMARY KEY,
    input_label TEXT);
    ''')

# creating the predictions table
cur.execute('''
    CREATE TABLE predictions (
    ID SERIAL PRIMARY KEY,
    prediction TEXT);
    ''')

# train the model and store it for this script
import main
model = main.model


#Load and store the sample image from data

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
    (sample_bytes, )

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
    (sample_bytes, )

#executing query
cur.execute("select * from input_data;")
print ("The sample input tested:")
print(cur.fetchall())


cur.execute("select * from predictions;")
print ("The produced prediction from the tested sample:")
print(cur.fetchall())


#commit data to db
con.commit()


con.close()





