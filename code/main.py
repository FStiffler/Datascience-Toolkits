# load all required libraries

# define parameters
num_classes = 10
input_shape = (28, 28, 1)
batch_size = 1000
epochs = 1

# load data
from data_load import load_data
x_train, y_train, x_test, y_test = load_data()

# prepare data
from data_prepare import prepare_data
x_train, y_train, x_test, y_test = prepare_data(x_train, y_train, x_test, y_test, num_classes)

# train model
from train_model import train_model
fitted_model = train_model(x_train, y_train, input_shape, num_classes, batch_size, epochs)
