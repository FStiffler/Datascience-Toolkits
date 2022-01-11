# import libraries
import os

# define all parameters for following steps
num_classes = 10  # number of digits to be classified (for mnist dataset 10)
input_shape = (28, 28, 1)
batch_size = 128
epochs = 5
model_name = "mnist_convnet_model.h5"  # how the model shall be named
model_save_dir = os.path.join(os.getcwd(), 'saved_models')  # relative path to save models in
eval_number = 5  # number of pictures to be shown to evaluate success of predictions

# load data
from data_load import load_data
x_train, y_train, x_test, y_test = load_data()

# prepare data
from data_prepare import prepare_data
x_train, y_train, x_test, y_test = prepare_data(x_train, y_train, x_test, y_test, num_classes)

# train model
from train_model import train_model
model = train_model(x_train, y_train, input_shape, num_classes, batch_size, epochs)

# evaluate model on test set
from evaluate_model import evaluate
evaluate(x_test,y_test,model)

# save model into h5 file in defined location
from handling_model import save_model
save_model(model, model_save_dir, model_name)

# load model in defined location for predictions
from handling_model import load_model
model = load_model(model_save_dir, model_name)

# make predictions based on model and test set and evaluate predictions
from predictions import predictions
predictions = predictions(model, x_test, eval_number)
