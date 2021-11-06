# import libraries
from tensorflow import keras

# function to load data
def load_data():
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    return x_train, y_train, x_test, y_test

