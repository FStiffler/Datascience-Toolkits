# Report: Milestone 1

## General Remarks

In Milestone 2 general rules for the collaborative work on the project were introduced. In the following you'll find the rules and our comments on how we guarantee compliance with the rules:

- *The branching strategy is consistent and no direct pushes to the master/main branch*

We never work on the master branch directly. For each milestone we created a new branch and based on that branch further branches if necessary. Even if we worked on the master branch by mistake, pushing to the master branch was not possible. This functionality was turned of in the Github settings before we even started  working on the projects.

- *All pull requests to master/main are reviewed by the other team member (add at least one comment to the review)*

We already did this on milestone 1 and will do so for all upcoming milestones. Again the settings on Github were set accordingly. Pull requests have to be reviewed and approved by the other team members. Just then it is possible to merge a pull request in the master branch. Without review and approval, the pull request is blocked from merging.

- *From now on, all versions in the pip "requirements file" are pinned (they have a fixed version)*

See Task 5

- *No python packages are installed with superuser rights (sudo), or equivalent in other operating systems*

After pip was already installed in the first milestone, it is no longer necessary to even use superuser rights to install new libraries. Every package can be installed via the command `pip install`

- *For each of the python packages you add to the requirements file, include the SHA256 hash digest to a table in the report (remember PyPI?)*

See Task 3 and Task 5

- *Use PEP8*

We studied the [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

## Task 1: Clean repository

### Branching

As already mentioned above, our default branch is the *master* branch. We never work on this branch but create new branches to work on during a milestone. We can locally create and checkout branches with the following commands:

```sh

$ git branch <new_branch_name>
$ git checkout <new_branch_name>

```

The next step is to push the branch to our remote repository as well.

```sh

$ git push -u origin <new_branch_name>

```

Now that the branch is available on the remote repository, somebody else can fetch all the changes including the newly added branch on the remote repository.

```sh

$ git fetch origin

```

A reference to the new branch is now stored locally and by checking out the branch we can work on it.

```sh

$ git checkout <new_branch_name>

```

Just by that, we have created a local working copy of the remote branch which was initially pushed by someone else.

Whenever we create and merged a pull request into the master branch and also create a release tag, we delete the branch used to work on the milestone directly in Github. This is synonymous with deleting the remote branch. This guarantees a cleaner repo and prevents a complicated work tree. Despite being deleted remotely on Github, the branch is still present locally in our repos. To delete a branch which is no longer used the following command can be used:

```sh

$ git branch -d <branch_name>

```

After that our repository is again in the exact same state as our remote repository on Github.


### Gitignore

#### What is a gitignore file?

Gitignore files allow us to define file types and whole directories in our repositories which must not be tracked by git. Whenever a new file is added to the git repository locally, git will track that file and list it as an uncommitted change. However, this file might be a picture, video or some other, non textual file which we really should not push to Github. To prevent git from tracking certain file types, we can add a new line to the gitignore file with the following, general syntax

```
*.<filetype>
```
With the asterisk in front of the file type, we just make sure to exclude all files of certain type no matter the actual filename. The filetype is identified by its file extension like for example .mp3, .mov, .tiff or .png. To exclude whole directories, we can use the following syntax.

```
<directory_name>/
```
This is especially useful if we, for example, store our python environment within the git project folder. Whenever a virtual environment is created in a project folder tracked by git, git recognizes the new directory with all python libraries, executables and all the other files necessary to run the environment. But it does not make any sense to push a local environment to Github. With the command above, we can simply stop git from tracking our environment. This way, everybody can set up a personal environment, add it to the gitignore file and by that prevent it from being tracked. We could also think of the possibility that we have to store large amount of data in our repository which we do not want to push due to the size. When we create a data folder and exclude it from being tracked, everybody can download the data manually in the data folder into his or her repository and work with it. While the files to work with the data is tracked and shared via Github, the data is only stored locally.

**Attention:**
It is really important that the folder which is not be tracked is named the same on all local repositories. If person 1 has a folder mydata which was added to the gitignore file and person 2 has a folder data, the folder of person 2 is still tracked which means he either has to rename his folder to mydata or he adds his folder to the gitignore file as well. The first solution is the more elegant one though.

#### How to create a gitignore file?

We already created a gitignore file before we started working on the milestones. This was done with the command `touch .gitignore`. To work on the file, one can use any text editor. We work with *atom* on this project. With `atom .gitignore` the gitignore file is opened in  atom and it is possible to add "ignores". As of now, our file contains the following "ignores":

- Our virtual environments
- .idea directory which is created by pycharm when starting a new project in a directory

#### Strategy to work with gitignore file?

The gitignore file itself can be modified and pushed to the remote repository which allows collaborators to pull the changes. Therefore, it is important to push the gitignore changes as soon as they are made. There are different work cases which can occur and which require different handling of the gitignore file.

1. **Working on the same branch consecutively**

If two or more collaborates work on the same feature branch in a consecutive fashion, they have to pull the most recent changes from the remote repo so that the gitignore file is up to date.

```sh

$ git pull

```
After that they can work normally and push possible changes to the gitignore file for others to pull again.

2. **Working on the same branch simultaneously**

If two or more collaborates work on the same feature branch simultaneously, they have to push their changes to the remote repo. If a merge conflict arises because both have changed entries in the gitignore file, atom can be used to resolve the conflict.


3. **Working on a different branch**

If two or more collaborates work on different feature branches, they must be merged eventually (creating a pull request) before they can be merged back into the master branch. Merge conflicts need to be resolved. After the two feature branches are merged, the gitignore file should contain "ignores" from both branches and therefore ignore the correct files for all collaborators.

Since we created only one feature branch per milestone we will run into case 1 and 2 a lot.



### Task 2

**Q1. What is a Hash function? What are some of the use cases?**

A hash function is a python function that converts any input value into a fixed size integer, aka the hash value. This integer identifies with a particular value and is very useful, as it enables quick look-up and/or comparison of values in large datasets by returning the hash value of the requested object. The hash function can only take a single parameter, although the hash value can be returned in a range of forms, i.e. integers, strings, or floats. Equal inputs also always receive the same hash value.

For a specific example, one may think of some sort of a "digital fingerprint" of some input. One may also consider the method of geographical coordinates assignment - each specific point on the surface of the Earth has its own unique numeric identifier, which greatly simplifies and speeds up the process of looking it up or locating it. As to our project at case, GitHub creates the exact same unique identifier each time a new commit is registered.

**Q2. What is a Python module, package and script? How do they differ from one another?**

A python script is a python file that contains the code, i.e. the entirety of all the symbols and their variations and/or combination that, taken together, constitute a single or a sequence of commands. The script is intended to be run directly.

A python module is also a python file, but the one that has to be imported into python scripts and/or other modules. These modules (or libraries) come with their own built-in functions, variables and classes.

A python package is a collection of the aforementioned modules that is designed to provide certain functionality to the combination of certain modules. Very often such packages come in the form of folders, out of which these modules can be important in a regular way; however, package folders also have a special ```init.py``` file that signals to Python that it is a multiple-module containing package.

**Q3. How would you explain a Docker container and volume to a child?**

In the simplest of terms, a Docker container is a box that contains an application and all the operative information. Such containers are also separate from each other, yet have certain communication channels for limited connection.

A Docker volume, however, is a detachable system for internal connection between containers and for manual adding/deleting of data from a container. This could be compared to some "sleeve" that might be used to take something out of a box or add some items into it.

**Q4. What is your preference concerning the use of Python virtualenv and Docker? When would you use one or the other?**

It is very hard to make such choice at this point, because we have not had sufficient exposure to either one of the options, Docker even more so. However, the experience with virtualenv that we have had allows us to come to a preliminary conclusion that Python virtualenv only keeps dependencies, whereas with Docker it is possible to store the entire "universe" of code. Furthermore, when using virtualenv, the code might be broken if used on a machine with a different python version; Docker, however, allows to install the correct version of python inside a specific container, thus avoiding that problem.

**Q5. What is the Docker build context?**

```
$ docker build [OPTIONS] PATH | URL | -
```
The Docker build context allows to build Docker images from a file and a context. That context, in its turn, is a set of files with specified locations - ```PATH``` or ```URL```, as seen in the command. The build process can refer to any of the files in the context.

**Q6. How can you assess the quality of a python package on PyPI?**

By checking the GitHub statistics, one may check the quality and rated reliability of certain python packages. Such statistics may include the number of stars, forks and/or open issues.


## Task 3: Code functionality

### Adding new functionalities

In this task we had to make sure that the code has the following functionalities:

1. Can load data
2. Can train (fit) a neural network on the data
3. Can save a fitted model to a ".h5" file
4. Can load a ".h5" file, using Keras
5. Can perform predictions using a "fitted" model, using Keras

The file *mnist_convnet.py* which we downloaded in milestone 1, has already the first two functionalities. The other three functionalities still needed to be added to the file. It makes sense to save the model after it is trained and evaluated which is why the third functionality was directly added to the *mnist_convnet.py* with the following line of code added to the file.

```
model.save("mnist_convnet_model.h5")
```

This command stored the model to a ".h5" file type in our working directory which was set to the root folder of the repository. Since we should not version control trained models, we added `*.h5` to our gitignore file. It is also to mention, that according to the [keras documentation](https://www.tensorflow.org/guide/keras/save_and_serialize), saving a model to a h5 file type this is an old way of saving a model(compared to the newer, simple `model.save()` command). The problem of h5 is that it does not store every single model component. For example external losses and metrics.

Now that the model was saved, we had to make sure to add the functionalities 4 and 5 as well. For this purpose we created a new python file *model_load.py*. This file loads the libraries *keras* and *numpy* and the same training and test data as in the *mnist_convnet.py* file. However, in the next steps we decided to only prepare the test data for prediction since the model was trained on the training data. Here again the same code as in *mnist_convnet.py* was used. The model is then reconstructed from the h5 file with:

```
reconstructed_model = keras.models.load_model("mnist_convnet_model.h5")
```

With this step we successfully added functionality 4. After that we wanted to add functionality 5. The reconstructed model should predict our test data. To do that we used the command:

```
pred = reconstructed_model.predict(x_test)
```

The part after the equal sign assigns each digit (0-9) a probability based on the handwritten digit depicted on the picture. The probabilities sum up to one but the number with the highest probability is the final prediction. This is done for each picture separately. The resulting ndarray has therefore 10'000 entries (number of pictures) with 10 probabilities each (for each digit one). The ndarray is assigned to the variable *pred*.

### Problems when testing functionalities

We tried to add and run a loop which would show the first nine pictures of the mnist dataset and show the according prediction to verify that it works. For this we installed matplotlib and we found a [code](https://www.askpython.com/python/examples/load-and-plot-mnist-dataset-in-python) which would show the pictures accordingly. But when we tried to run matplotlib we got an error

```
UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
```

The figure was not displayed. So we tried to install *tkinter* as was stated [here](https://stackoverflow.com/questions/56656777/userwarning-matplotlib-is-currently-using-agg-which-is-a-non-gui-backend-so). But after that our file did not run anymore and we got other errors as well. Therefore we decided to remove the current virtual environment and create a new one with the requirements file from Task 5. After that we reinstalled matplotlib and magically everything was fine. We had probably installed incompatible packages in the old environment which caused the errors.

### Final solution

In the final solution it is possible to run the *mnist_convnet.py* file to fit the model and save it to a h5 file. After that we can run the *model_load.py* file to predict the digits on the test set. To verify the code, a loop runs over the first ten pictures. It shows one picture at the time by automatically opening the matplotlib UI and prints the prediction to the picture into the console. Then the code opens the next picture and so on.

**Attention**:
Make sure that the console is not covered by the matplotlib interface when running the code otherwise you won't see the actual predictions

## Task 4: Modularize code

### Structure of repository

Since we are required to create several modules which would look pretty messy if they were all stored in the root folder, we created a new directory called *code*. All the modules are to be stored in this directory.

### What modules to build?

For the purpose of modularizing our code we had to think about how we could possibly split our code into meaningful parts. For that purpose we opened the files *mnist_convnet.py* and *model_load.py* from the previous task to gain an overview over the different steps conducted in the code. We identified the following steps:

1. Loading data
2. Preparing data
3. Building and training the model
4. Evaluating the model
5. Saving the model
6. Loading the saved model again
7. Making predictions and verify them

We knew, we had to create modules which would complete all these steps individually and can be run from the the *main.py* file. So we started creating the according modules in the *code* directory. We also directly created our *main.py* in order to test out the different modules right away.

#### 1. Loading data

We created a file *data_load.py* and added a function `load_data()` to load the data. We used the exact same code to load the data as in *mnist_convnet.py*. After that we tried to import the function to the *main.py* file by adding the following code:

```
from data_load_prepare import load_data
load_data()
```

However we recognized two problems. First we were not able to find the file *data_load.py* and consequently to import the function. To solve that we had to define the *code* directory as a source folder. After that pycharm recognized the file and we could load the function. But the next problem awaited. The function to load the data relies on keras and although we loaded keras in our *main.py* file, we were not able to load the data. Therefore we had to import keras already in *data_load.py*. After that everything worked fine. The function allows the loading of the data into the *main.py* file.


#### 2. Preparing data

Initially we thought we can use the same file to prepare and load the data. However, that was not the case because we had to call the functions consecutively. So we created a new file *data_prepare.py* with the function `prepare_data()` based on the code from the *mnist_convnet.py* file. We made sure that the output of `load_data()` is going to be the input of `prepare_data()`. An additional input is the number of classes which is set at the beginning of the *main.py* file. The output of `prepare_data()` is the prepared data. By importing this module function into the *main.py* file, we can generate the prepared data.

#### 3. Building and training the model

Upon first review, we thought that we have to separate model creation and model training. But considering the code in more detail we decided to combine those two steps which is why we adjusted also the list above. We created a new python file *train_model.py*. This file contains the function `train_model()`. This function creates the model conceptually with all of its layers and fits the model to the training data. The inputs are the "x_train" and "y_train" outputs of `prepare_data()` called in the previous step. Additional inputs are the variables "input_shape", "num_classes", "batch_size" and "epochs" which are defined in the *main.py* file directly. Again by importing the module in *main.py* we can train the model based on the data obtained in previous steps.

The first time wen ran the file, my virtual machine hang up. So we had to restart it. To prevent our machines from hanging up again, we had increased the batch size and reduced the number of epochs (changed the according parameters in the file directly).

#### 4. Evaluating the model

We created a file *evaluate_model.py* with the function `evaluate()`. The function takes the fitted model and the test data as input to create an evaluation score which is printed to the console. As with all the previous steps, we simply copied the corresponding code of the *mnist_convnet.py* file. We implemented this function into *main.py*.

#### 5. Saving the model/ 6. Loading the saved model again

We thought it would be reasonable to create one module to do both, save a model into a h5 file and load it again. Therefore we created the file *handling_model.py*. It has two functions. The function `save_model()` which allows to save a model under a directory relative to the root directory and with a specific name. Both directory and name are defined in *main.py*. The relative directory, therefore, is concatenated from the working directory and a string. The second function `load_model()` allows to load a previously saved model from a specific location. The code for both functions stems from the *model_load.py* file from Task 3.

When we ran the file, we got an `permission denied error`. We realized that we made an error when joining the relative path. We corrected the mistake and ran the code successfully after that.

#### 7. Making predictions and verify them

Finally we created the file *predictions.py* to make predictions based on an input and a model. The file contains the function `predictions()` which takes the previously loaded model and the test data as input. Furthermore we have to define how many pictures of the test data with according predictions we want to show. The function returns the predictions for the test data and shows the predefined number of pictures with predicted digit in the console.

### What happens to the old files?

With the work we did so far, the two files *model_load.py* and *mnist_convnet.py* are now successfully decomposed into modules and are no longer needed. Therefore we created a folder for these two files named *original*.


## Task 5: Virtual environment and requirements files

### What are virtual environments?

As we mentioned already in our milestone 1 report, some of us already worked in a virtual environments. A virtual environment allows us to work with different dependencies on each project. We might need numpy 1.18.1 for one project but numpy 1.19.1 for another one. In this case virtual environments provide an solution to this problem. We can create two environments with two different versions of numpy and when working on a project, we just activate the one with the correct numpy version.

### How can we set up a virtual environment?

For the purpose of demonstration, we set a new environment from ground and assumed that nothing is preinstalled yet. Therefore, we needed to have pip available before we could even install the virtualenv library which in turn would allow us to install and create virtual environments. For this purpose pip was installed first:

```
sudo apt-get install python3-pip
```

With pip available we could install the virtualenv library:

```
pip install virtualenv
```

Now everything was ready to create a new environment. First of all we had to think of the directory where we wanted to create the virtual environment. It totally makes sense to create the environment within the project directory for which the environment is needed. This, however, implies that we have to prevent git from tracking changes to the virtual environment. Therefore we have to add the environment directory to the gitignore file. For this, please refer to Task 2. For this example we wanted to do exactly that. So we changed our local directory to the project directory and used the following command to create the environment:

```
virtualenv <environment_name>
```

The environment is created with the default python version installed on the computer. But we could also define other python versions to use in the environment: as long as we have downloaded and saved them somewhere:

```
virtualenv --python=<Path_to_python_executable> <Path_to_workingdirectory>
```

Now that the virtual environment was created we could activate it with

```
source <environment_name>/bin/activate
```

The virtual environment was now activated and we were able to install libraries.

### How can we make a requirements file work with the virtual environment?

In mileston 1 we described which packages are actually necessary to run the [mnist_convnet.py](../original/mnist_convnet.py) file. Based on these dependencies and further dependecies required for the [main.py](../code/mnist_convnet.py) we were able to create a [requirements.txt](../requirements.txt) file in the Github root folder. To create the file we made sure to set our locally directory to the root folder and then we used the Linux command:

```sh

$ touch requirements.txt

```

This created a empty text file. To retrieve the relevant information about the dependencies, we activated our old python environments (when there were any already) and called `pip list`. Because we installed all required libraries already in milestone 1 and successfully ran the code with said libraries and library versions we could simply copy the names and versions. The two values were pasted into the *requirements.txt* file. Each line contains one required library and the according version separated by *==*. These libraries are not yet installed in our new environment which is why we deactivated the old environment and reactivated the new environment we just created previously (again make sure to set the correct working directory). Based on this requirements file we could now install all the needed packages also into the new environment by running:

```
pip install -r requirements.txt
```

The packages were installed smoothly. And because they were now available in the new environment, we could simply navigate to the *main.py* file and run it with `python3 main.py`. No errors were raised. The required packages were also added to the README file in the root folder under the section *Requirements*.


## Task 6: Dockerizing the model

1. To install docker onto our machine, we first need to give out a few commands in the terminal:

```
$ sudo apt-get update

$ sudo apt-get install \
   ca-certificates \
   curl \
   gnupg \
   lsb-release

$  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
and lastly, set up a stable repository
```
$ echo \
 "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
 $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

There is also another way to install Docker Engine, as is instructed on the Docker Docs:

```
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```
and if one were looking for a specific version of Docker:
```
$  apt-cache madison docker-ce
$ sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
```

After the installation, it is important to verify whether the process has been finished correctly by running a test command.

```
$  sudo docker run hello-world
```

For us everything worked smoothly so far, so we continued to set up docker.
However, it is tedious to have always to use `sudo` because our user account has not the required privileges. Therefore we added root user privileges to our standard user.

```
sudo groupadd docker

sudo usermod -aG docker $USER

newgrp docker

docker run hello-world
```

The test command ran successfully.

2. Before starting to work directly with our model and engaging it with a docker container, we decided to try out the docker functionality and followed the set up and run instructions from Docker Docs with their test app. This helped to better understand the basic commands and functions of Docker, as well as allowed us to prepare ourselves for writing our own Dockerfile later.
To do this, we followed several steps:
  1. To initiate the set up process after successful installation, we created a directory for a test project, following the instructions form Docker Docs.
    ```
    $ mkdir composetest
    $ cd composetest
    ```
  Then we had to create a file in a separate text/code editor, naming it ```app.py``` and saving in the test project directory with the given code:

    ```
    $ import time

    $ import redis
    $ from flask import Flask

    $ app = Flask(__name__)
    $ cache = redis.Redis(host='redis', port=6379)

    $ def get_hit_count():
        retries = 5
        while True:
          try:
            return cache.incr('hits')
              except redis.exceptions.ConnectionError as exc:
              if retries == 0:
                  raise exc
                retries -= 1
            time.sleep(0.5)

    $ @app.route('/')
    $ def hello():
      count = get_hit_count()
      return 'Hello World! I have been seen {} times.\n'.format(count)
    ```
    This had to be followed by another file creation, this time ```requirements.txt``` containing only ```flask``` and ```redis```, with the latter being the hostname of the redis container on the network.

    2. Having set the groundwork for dockerization, we could now move on to creating a test Dockerfile that will build the Docker image in the end. The Dockerfile is where all the dependencies are stored to be later used by Python.

```
# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```

  This code contains information for Docker about which Python version to use with this Python image, sets directory to ```/code```, copies the current directory to the working directory in the image and sets the command for the container.

  One more important file to create before composing a Docker container is the ```docker-compose.yml``` file:

```
version: "3.9"
services:
  web:
    build: .
    ports:
      - "5000:5000"
  redis:
    image: "redis:alpine"
```

  This had to be pasted into an empty file in our text editor, specifying the ports to be used by Docker.
  Now we are ready to start the test application.

  3. Building and running the test Docker app

  By executing the ```$ docker-compose up``` command in the terminal, the machine starts pulling all the lacking locally information and creating the image for our given code whilst starting the processes we defined earlier in the prerequired files. This takes some time when being run for the first time.

  Having waited long enough for the machine to finish the task, one may type in ```https://localhost:5000/``` in ther browser and check whether the code worked or not. If everything has been done correctly, like in our case, a "Hello World! I have been seen 1 times." message should appear on the screen. The number of views should change with each time the page is refreshed.

  To check whether there are any other local images present, we simply used the
```
$ docker image ls
```
  to list all local images with their respective repositories, tags, image IDs etc.

  To stop the application from running, a ```docker-compose down``` command or a Ctrl+C combination would suffice.

  4. One step further that we took was adding the bind mount to the test app by editing the ```docker-compose.yml``` file:
```
version: "3.9"
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/code
    environment:
      FLASK_ENV: development
  redis:
    image: "redis:alpine"
 ```

  The added ```volumes``` key mounts the project directory to /code inside of the container, taking away the obligation to rebuild the image each time the code must be changed.

  After this, the only steps left in running our test app was to re-build and run the app with already beknownst to us command ```docker-compose up```. We also followed the suggestion from Docker Docs, and modified the app.py file, so that its greeting message sounded differenly:

 ```
 return 'Hello from Docker! I have been seen {} times.\n'.format(count)
 ```

3. Having completed the Docker rookie initiation, we decided we were finally ready to create our own docker container and Dockerfile. We carefully wrote the **Dockerfile** and even **docker-compose.yml**, saved the updated **requirements.txt** to the correct directory, and retraced every step we have completed in the Docker training. However, upon attempting to complete the **docker run** command with our python file (i.e. training model), we kept getting an error
```
Top-level object must be a mapping
```
The **docker-compose up** command was returning the same error message over and ever again, so we checked our Dockerfile for errors multiple times, editing every minor detail and re-running the command, but to no avail. So, then we turned to online community sources for help. However, neither generic google nor stackoverflow forums did not manage to shed any light on the issue we were having, as it was clearly a problem with the newest Dockerfile code, since before we started dockerizing our own model, Docker was running smoothly.
So we decided to take a completely another approach, which proved to be a lot more successful. Time to dockerize our model!

4. *Happy ending to a confusing story*
 In order to create a docker container we first looked at potential docker images of use on dockerHub. Therefore we created an account to have access to the images. An useful image might be the official python image. We downloaded it with `docker pull python`. By that, the docker image was available on our system.

The next step was to create the docker file in our local repository. The docker file can be used to create a docker image which can build a container. We creatd a new file with `touch Dockerfile` and added the following code:

```
FROM python:3.8

WORKDIR /app

COPY code/main.py
COPY code/main.py
COPY code/main.py
COPY code/main.py
COPY code/main.py
COPY requirements.txt

RUN pip install -r requirements.txt

CMD python main.py
```

Then we ran `docker build .` to create an image. However we got an error message:

```
Sending build context to Docker daemon  2.674GB
Error response from daemon: dockerfile parse error line 5: COPY requires at least two arguments, but only one was provided. Destination could not be determined.
```

We realized that we forgot to define the `<dest>` of the copy command. Therefore we added the new working directory for our docker container to the file as destination expressed by a single point.

```
FROM python:3.8

WORKDIR /app

COPY code/main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD python main.py
```

We reran `docker build .`. But now we got the following error message:

```
ModuleNotFoundError: No module named 'data_load'
```

Now it was clear that we had to add every single module to the image (Which makes kind of sense). So we did that.

```
FROM python:3.8

WORKDIR /app

COPY code/*.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD python main.py
```

We reran `docker build .`. But we got another message:

```
When using COPY with more than one source file, the destination must be a directory and end with a /
```
We made further changes to the docker file:

```
FROM python:3.8

WORKDIR /app

COPY code/*.py modules/
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD python main.py
```

And of course we got another error after have successfully built our image and tried to run a container.

```
python: can't open file 'main.py': [Errno 2] No such file or directory
```

It can't run *main.py* because it is not in the directory `/app ` but in `/app/modules`. So we changed the code again.

```
FROM python:3.8

WORKDIR /app

COPY code/*.py modules/
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD python modules/main.py
```

Now the image was built succesfully. We were also able to run the image to create a container with the command `docker run <image_id>`. But we realized that our image had no image name and tag when we looked at the images with `docker images`. So we recreated the image with `docker build -t milestone2:v1 .`. After that we can run the image to create a container named 'milestone2' with `docker run --name milestone2 milestone2:v1`.
