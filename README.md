# Data Science Toolkits & Architectures Project

## Introduction
This is the repository of our Data Science Toolkits & Architectures Project
at the University of Lucerne.
The collaborators are Monica Perez, Kateryna Myskova and Flurin Stiffler. Together, we have to work on milestones in which we learn the tools and architectures necessary to successfully accomplish a data science projects. In the following chapters, the milestones are described.

## Documentation

### Milestone 1

In the first milestone, we had to set up our github repo and we were assigned [data](http://yann.lecun.com/exdb/mnist/) as well as a [codebase](https://github.com/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.py).

In the following steps, we explain how the codebase can be run on a computer with Ubuntu 20.04.

1. Download codebase:

```sh

$ wget https://raw.githubusercontent.com/keras-team/keras-io/master/examples/vision/mnist_convnet.py

```

2. Activate python environment (if available):

```sh

$ source <env_name>/bin/activate

```

3. Install pip (just if not installed already):

```sh

$ sudo apt-get install -y python3-pip

```

 4. Update pip (if not done already):

```sh

$ pip3 install --upgrade pip

```

5. Install required library:

```sh

$ pip3 install tensorflow

```

 4. Run the file:

Now that everything is ready, we can run the file:

```sh

$ python3 mnist_convnet.py

```

A more detailed report on milestone 1 can be found [here](Reports/report1.md)

## Requirements

### Python packages (including hashes)

numpy == 1.19.5 \

keras == 2.6.0 \

tensorflow == 2.6.0 \

matplotlib == 3.4.3 \


## Milestone 2

In the second milestone, we got acquainted with Docker, set up the necessary model training files and actually trained the neural network.

Firstly, we double-checked the .gitignore files to make sure version-control is working on all machines for all contributors. Secondly, we adapted the code to have all the required functionality, i.e. it could load the data, fit a neural network on the data, load a *.h5* file using Keras, and perform predictions using a fitted Keras-based model. We also had to modularize our code, so that its structure would be more maintainable and PEP8 conforming.

Our next step was to create the **requirements.txt** file and download all the required packages in a virtual environment. The aforementioned requirements file would be of great help later on to quickly download the required packages in other envs.

Lastly, we got acquainted with Docker, having installed and set it up on our machines. Although not without extra issues, we managed to create our images and make it run our code.
