# Import packages
import psycopg2
from tensorflow import keras
from PIL import Image
import pickle

# Import already existing module to load data
from data_load import load_data

# load data
x_train, y_train, x_test, y_test = load_data()

# take first picture of training data as sample
sample = x_train[0]

# Visualize picture
Image.fromarray(sample).show()

# Transform picture to byte stream
sample_bytes = pickle.dumps(sample)

# Establish connection to task3 DB
con = psycopg2.connect(
    host="localhost",
    port="5432",
    database="task3",
    user="admin",
    password="1234")

# Turn off transaction mode and enable autocommit
con.autocommit = True

# Creat cursor
cur = con.cursor()

# Create a new table
cur.execute('''
    CREATE TABLE pictures (
    ID int PRIMARY KEY
        GENERATED ALWAYS AS IDENTITY,
    Picture bytea
    )
    ''')

# Insert bytes stream
cur.execute(
    """
    INSERT INTO pictures (Picture)
    VALUES (%s)
    """,
    (sample_bytes, )
)

# Select transformed sample from DB and store it as python object
cur.execute('SELECT Picture FROM pictures')
sample_bytes_loaded = cur.fetchone()[0]

# Retransform to object
sample_back = pickle.loads(sample_bytes_loaded)

# Visualize picture
Image.fromarray(sample_back).show()

# Close connection
con.close()
