# import packages
from tensorflow import keras
from tensorflow.keras import layers
import wandb
from wandb.keras import WandbCallback

# define necessary parameters used in modules
num_classes = 10  # number of digits to be classified (for mnist dataset 10)
input_shape = (28, 28, 1)

# new run
wandb.init(project="dbs_container")

# set configurations
wandb.config = {
  "epochs": 5,
  "batch_size": 128,
  "validation_split": 0.1,
  "loss": "categorical_crossentropy",
  "optimizer": "adam",
  "metric": "accuracy"


}

# load data
from data_load import load_data
x_train, y_train, x_test, y_test = load_data()

# prepare data
from data_prepare import prepare_data
x_train, y_train, x_test, y_test = prepare_data(x_train, y_train, x_test, y_test, num_classes)

# define model
model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

# compile and train model
model.compile(loss = wandb.config['loss'],
              optimizer = wandb.config['optimizer'],
              metrics = [wandb.config['metric']])

model.fit(x_train, y_train,
          validation_data = (x_test, y_test),
          batch_size = wandb.config['batch_size'],
          epochs = wandb.config['epochs'],
          validation_split = wandb.config['validation_split'],
          callbacks = [WandbCallback()])
