# function to evaluate the model
def evaluate(x_test, y_test, model):
    """
    ## Evaluate the trained model
    """

    score = model.evaluate(x_test, y_test, verbose=0)
    print("------------------------")
    print("Model evaluation")
    print("Test loss:", score[0])
    print("Test accuracy:", score[1])