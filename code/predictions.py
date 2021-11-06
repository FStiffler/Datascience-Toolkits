# import libraries
from matplotlib import pyplot as plt
import time
import numpy as np

# function to make predicitons
def predictions(model, x_test, eval_number):

    # make predictions
    predictions = model.predict(x_test)

    # evaluate that predictions were made successfully
    for i in range(eval_number):
        # show handwritten digit
        print("Actual:")
        plt.imshow(x_test[i], cmap=plt.get_cmap('gray'))
        plt.show(block=False)
        plt.pause(1)
        plt.close()

        # get prediction for picture
        print("Prediciton:", np.argmax(predictions[i]))
        time.sleep(1)

    return predictions

