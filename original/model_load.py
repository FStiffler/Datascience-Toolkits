"""
## Setup
"""

import numpy as np
from tensorflow import keras

"""
## Prepare the data
"""

# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Scale images to the [0, 1] range
x_test = x_test.astype("float32") / 255
# Make sure images have shape (28, 28, 1)
x_test = np.expand_dims(x_test, -1)

# convert class vectors to binary class matrices
y_test = keras.utils.to_categorical(y_test, num_classes)

"""
## Import model
"""
reconstructed_model = keras.models.load_model("mnist_convnet_model.h5")

"""
## Predict data
"""
pred = reconstructed_model.predict(x_test)


"""
## Small loop to look at pictures and predictions
"""
from matplotlib import pyplot
import time
for i in range(9):

    # show handwritten digit
    print("Actual:")
    pyplot.imshow(x_test[i], cmap=pyplot.get_cmap('gray'))
    pyplot.show(block=False)
    pyplot.pause(1)
    pyplot.close()

    # get prediciton for picture
    print("Prediciton:", np.argmax(pred[i]))
    time.sleep(1)




