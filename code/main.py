# load all required libraries

# define parameters
num_classes = 10

# load data
from data_load import load_data
x_train, y_train, x_test, y_test = load_data()

# prepare data
from data_prepare import prepare_data
x_train, y_train, x_test, y_test = prepare_data(x_train, y_train, x_test, y_test, num_classes)

