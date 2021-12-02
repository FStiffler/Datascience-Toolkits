# Report: Milestone 4

## Task 1

The first step was to create an account on [Weights&Biases](https://wandb.ai/site). After that we worked through the proposed tutorial under this [link](https://colab.research.google.com/drive/1pMcNYctQpRoBKD5Z0iXeFWQD8hIDgzCV).

### Questions

**1. What is Experiment Management and why is it important?**

Experiment Management is a solution to the problem of increasing complexity and volume of operated data in various projects, especially in Machine Learning. Therefore, with more and more tasks completed the rapidly growing number of experiment data, hyperparameters, datasets etc is getting harder to track and manage, so EM comes in handy to tackle this issue.

EM is used to track all the experiments that have been completed in order not to lose knowledge, preserve efficient management of resources, and avoid time waste. Those experiments usually come in a 5-step process, i.e. hypothesis formulation, variable definition, trainig dataset and parameter tracking, trial creation and training launch, and finally result analysis. After completing the experiment (or a whole range of those), EM can also be used for knowledge sharing, as others (team members, colleagues etc) may need to reproduce one's own experiments.
In the case with Machine Learning, where experiments are designed, to navigate the huge space of possible experiments with hundreds of parameters, it is important to resort to Experiment Management.

**2. What is a Metric in ML?**

In ML, the summarized outcome in a single or a couple of numbers is called a Metric. It is primarily used for comparing experiment outcomes, measuring and monitoring the performance of a particular model. For ML, however, for comparative measurement of accuracy, precision etc of the outcome, depends also on the Metric chosen for usage, i.e. one ML model can get different measurement results depending on the Metric applied.

**3. What is Precision and Recall? Why is there often a Trade-off between them?**

Precision and Recall are both the Metrics used in ML, where Precision is a measure of proportion of the tests classified correctly of all positively classified ones. Basically, this is the measure of how to-the-point the model's calculations appeared to be. Recall is another Metric that describes the opposite of Precision, i.e. the percentage of incorrectly classified cases of all actual positive test cases.
Therefore, given the information just provided, it is evident that some kind of a tradeoff must exist between the two, as they are in a way mutually excluding. If one was wishing to focus on minimization of False Negatives, one would get higher levels of Recall while keeping their Precision levels lower. Vice versa, if one were willing to aim at keeping Precision levels at their highest, one would have to agree to having their Recall level low (albeit not too bad), thus minimizing False Positives.


**4. What is AUROC Metric?**

AUROC is the acronym that stands for Area Under Receiver Operating Characteristic Curve, and includes both the AUC and ROC terms within, where the ROC is a probability curve, and AUC represents the degree of separability. It is a performance measurement metric that shows how well the given model is working with classification problems at various threshold settings. The higher the ROC curve is, the better the model is at predicting classes; the better the model, the smaller the shared area of both distributions becomes. Overall, the main purpose of the AUROC metric is to tell about the model's ability to discriminate between positive cases and negative non-cases. The closer AUROC gets to 1, the better discriminatory ability the model has.

**5. What is a Confusion Matrix?**

Confusion Matrix is a popular visualization method and/or metric of prediction inside a classification problem, where the output can be of two or more classes, giving the matrix an actual output and describes the performance of the model. The easiest example would be the binary CM with True/False Positives and True/False Negatives, where the ideal model should produce O False Negatives and Positives, yet such a result in real life is unattainable, as no model can reach 100% accuracy all the time.

## Task 2


### Instrument code without docker container

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

### Instrument code with docker container

Now that we had a code which allowed us to make test runs and track the model training with different parameters on W&B, we wanted to dockerize everything. The docker container has to login to W&B. For this purpose we created a .env file which contains our personal access key and is called `WANDB_TOKEN`. This file must never be tracked by git to prevent foreigners to access our account by looking at the key in the file. Therefore we added the .env to the gitignore file. Next up, we had to create an entrypoint script which is executed in the entrypoint of the docker container when the docker image is run. The script allows us to login to W%B before the actual CMD command in the docker file is executed. Therefore, we created the file `docker_entrypoint.sh` and inserted the proposed code in the milestone description:

```
#!/bin/bash

set -e

wandb login $WANDB_TOKEN

exec "$@"
```

In a last step we had to create the docker file itself. For this purpose we adjusted the already existing docker file in our root folder. We decided to go back to a docker file solution in which we copy the modules into the container instead of mounting the working directory on the container (as we already did in milestone 2). We thought it was just easier to do when there is no additional docker compose file which would mount the current working directory to the container. We also had to define the ENTRYPOINT command. The docker file was the following:

```
FROM python:3.8

WORKDIR /app

COPY requirements.txt .
COPY docker_entrypoint.sh .
COPY code/*.py modules/

RUN pip install -r requirements.txt

ENTRYPOINT ["sh","docker_entrypoint.sh"]

CMD python modules/wandb_test.py
```

Last but not least we made a small adjustment to our python file to be executed by the docker container. When we tested the python file before, we created a project called `dst` on W&B. To test the docker container we planned to create a new project `dst_container`. Hence, we adjusted the relevant line in our code. Now we were ready to build the image from the dockerfile with `docker build -t wandb:v1 .`. After that we had to run `docker run --name wandb --env-file=.env wandb:v1`. Because the batch size was still set to 128 and epochs to 5, running the container again took a while. But eventually everything worked. We logged in to W&B again to see if the project was created and all the metrics where tracked. Everything was there just like before. The dockerized project on W&B can be found [Here](https://wandb.ai/fstiffler/dbs_container). There was one last issue we realized just later. In the python file, Flurin defined `entity=fstiffler`. But if somebody else now tries to run the container, it will not work if she or he tries to connect to her or his own W&B account since the entity does not exist. Here the explanation from [W&B](https://docs.wandb.ai/ref/python/init):

*'An entity is a username or team name where you're sending runs. This entity must exist before you can send runs there, so make sure to create your account or team in the UI before starting to log runs. If you don't specify an entity, the run will be sent to your default entity, which is usually your username.'*

So we removed this piece of code and rebuild the container with `docker build -t wandb:v2 .` and `docker run --name wandb --env-file=.env wandb:v2`. Visiting our account on W&B once again we saw, that everything worked fine again and the user was just the defined default user. With that, we successfully finished Task 2.

## Task 3

In order to even create a jupyter notebook in the first place, we had to install the notebook library. Accordingly, we activated our virtual environment and ran the command `pip install notebook`. After that, we simply had to type `jupyter notebook` into the terminal. This command opened up a browser window running on the localhost address. The window showed all the files in the local working directory from which the jupyter notebook command was executed. There was also a button to create a new notebook which we did. We saved the notebook `data_analysis.ipynb`. We commented all the analyses in the notebook directly, having first created several histograms to confirm the even distribution of labels, which we preassumed in Task 2 to go with accuracy as our evaluation metric. We realized that the creation of jupyter notebooks initiates a new working directory `.ipynb_checkpoints` which is tracked by git. So we had to extend our gitignore file once more. In the final step of our jupyter notebook we wanted to create a confusion matrix with the `sklearn` library. So we were required to install the package with `pip install sklearn`. After that, everything just worked fine and we were able to complete the analysis without any problems. 
