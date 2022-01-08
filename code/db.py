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
