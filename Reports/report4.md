# Report: Milestone 4

## Task 1

The first step was to create an account on [Weights&Biases](https://wandb.ai/site). After that we worked through the proposed tutorial under this [link](https://colab.research.google.com/drive/1pMcNYctQpRoBKD5Z0iXeFWQD8hIDgzCV).

### Questions

**1. What is Experiment Management and why is it important?**

**2. What is a Metric in ML?**

**3. What is Precision and Recall? Why is there often a Trade-off between them?**

**4. What is AUROC Metric?**

**5. What is a Confusion Matrix?**


## Task 2


### Running a simple project without docker container

we had a look at the [quickstart guide](https://wandb.ai/quickstart/keras) provided by Weights&Biases for Keras. The first step was to install the package `wandb`. So we activated our virtual environment and installed the package. We also added the file to package to the requirements file right away. The hashes were added to the requirements table in the README file. The next step was to login to `wandb`. To do that we typed `wandb login` into our terminal. There we had to add the API key which was found on our wandb account. That seemed to work without any problem. In a next step we created a `wandb.py` file in the same directory as the other code so that we could easily access already prepared modules for this task. We tried to follow the instructions online to import the required packages and modules but it did not work initially. We received an error message stating that wandb was not a package. It was just after that we realized, that this error occurred due to the file name `wandb.py`. So we changed the name to `wandb_test.py` and reran the file. We went to our wandb account and saw that first of all, a new project was initialized and that a run with a funny name was present. However, we still had some errors in our model which is why we had to adjust the code several times before we conducted our first successful run. We deleted all our unsuccessful runs right after that.

Our final code for the first successful run was the following:

```
# import packages
from tensorflow import keras
from tensorflow.keras import layers
import wandb
from wandb.keras import WandbCallback

# define necessary parameters used in modules
num_classes = 10  # number of digits to be classified (for mnist dataset 10)
input_shape = (28, 28, 1)

# new run
wandb.init(project="dbs", entity="fstiffler")

# set configurations
wandb.config = {
  "epochs": 1,
  "batch_size": 1000,
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
```

We chose the accuracy metric to evaluate our model since we assumed to have relatively balanced data set of all digits (0-9). But this also definitely something we were going to check in Task 3.
The code above fulfills all requirements according to milestone description:

- Login to W&B

We had to login to the account once from the terminal and were connected afterwards. So we did not have to login every time we reran the python file.

- Train a Model

The model is trained based on the configuration dictionary defined at the beginning of the file

- Save and upload the trained model

A h5 file of the best model is automatically saved and uploaded to our wandb account. It can be found when going on a run and then selecting the tab `Files` in the selection menu to the left.

- Log the value of the loss function (graphically)

In the same selection menu we can go on the `Charts` tab where we see the charts for different metrics. The loss was at 1.084.

- Log your metric (graphically), Tip use a Keras Metric

The accuracy of the test set evaluation was about 67%. This is not astonishing given that we only train the model in one epoch and use relatively larger batches. We set this parameter in milestone two do reduce run time of the `main.py` file but now it was time to change that.

We started a new run but this time we set the batch-size to 128 (which is the value often used to train neural networks) and epochs to 5. We hoped to see a massive improvement in accuracy doing that. This took some time to complete. After the run was completed, we checked out the result once again on our wandb account and saw that our accuracy has improved up to 98%. The loss was reduced to 0.06. The results from the previous run were also depicted in the charts of the second run which allowed a direct comparison. All in all, this were the results we were expecting and hoping for. The results can be viewed [here](https://wandb.ai/fstiffler/dbs?workspace=user-fstiffler).

We recognized that all the runs were also logged locally in our working directory where the `wandb_test.py` file was. Running the file would create a directory `wandb` with log files of every run. So we had to add this directory to our gitignore file to prevent it from being tracked by git. 
