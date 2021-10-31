# Report: Milestone 1

## Task 1: Data

The provided MNIST dataset is a subset of a large MNIST database, containing handwritten digits and divided into 4 separate files with both images and labels sets:

A training set of 60,000 examples and a test set of 10,000 examples.


The database was formed from two Special Databases (NIST's 3 and 1), with the former reported to be much cleaner due to the difference in study subjects' differences.
Merging the databases into a single one was crucial for drawing valid conclusions from the learning experiments conducted, while also having two independent sets of samples - i.e. training and test sets.


The file format constitutes original bilevel images, normalized to a 20x20 pixel box with their aspect ratio preserved;
  the aforementioned images also contain grey levels due to the anti-aliasing technique usage. The images were also centered in a 28x28 field.

Data is stored in a format designed specifically for vectors and multidimensional matrices, while all the integers are stored in the MSB first format.
  The test set examples were taken from different sets: first 5000 are from the original NIST training set, the last 5000 are from the original test set.
  It has also been reported that the first 5000 examples from the original training set are cleaner and easier to interpret than the last 5000.

The image file sets have the pixels organized row-wise and contain their values within the 0-255.0 range,
  where 0 means background (white) and 255 means foreground (black)
  As for the label file sets, both training and test sets have the labels values between 0 and 9.


The given data is stored using the IDX file format, suitable for vectors and multidimensional matrices of various numerical types.

The problem at hand to be solved by machine learning models is a classic example of a classification problem,
 as the goal is to classify each particular image in the dataset according to its label value attached (0-9)

## Task 2: Codebase

The code base which was assigned to us can be found [here](https://github.com/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.py). It is a python file from the Github repo of the keras-team. The provided URL of the codebase allowed us to download the file with the terminal command:

```sh

$ wget https://github.com/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.py

```

However, we recognized that we simply downloaded the source code of the Github page with this linux command. To actually download the python file with actual python code, we had to click on *Raw* on the Github page and copy the URL of the new webbrowser window. After that we reran the command above with the now correct URL.

The python file was stored in the local root folder of the our repository as *mnist_convnet.py*. The file was only stored in the root folder of the previously created *Milestone1* branch. The *master* branch stayed unaffected in this process. The next step was to commit and push the file to the same branch on the remote repo on Github.

## Task 3: Commit

The downloaded file had to be staged first before we could commit it:

```sh

$ git add mnist_convnet.py

```

Then the file was committed to our local repository with the command:

```sh

$ git commit -m <commit_message>

```

Finally, the file was pushed to the remote repo on Github:

```sh

$ git push

```

## Task 4: Run code

### Necessary steps to run the code

To run the code, first we had to activate our virtual python environment (if a virtual environment was even set up for this project). To activate the environment, the following command had to be used:

```sh

$ source <env_name>/bin/activate

```

After the environment was activated, we started installing libraries required to run the *mnist_convnet.py* file. Without the libraries, the file does not run properly and returns an error. To install libraries, we needed pip which allows access to libraries from the python package index (PyPI). To install pip, the following command was used:

```sh

$ sudo apt-get install -y python3-pip

```

We verfied the installation with:

```sh

$ pip3 --version

```

Some of us had pip already installed. But it was important to have the latest version. To achieve that, the following command was used:

```sh

$ pip3 install --upgrade pip

```

Now with pip available, we installed the required libraries directly into our virtual environments:

```sh

$ pip3 install tensorflow

```
 The *mnist_convnet.py* indicates that three libraries are about to be used, namely *tensorflow*, *keras* and *numpy*. The library tensorflow contains the keras API which is why, a separate installation of keras was not necessary. The numpy library comes with the tensorflow distribution as well. We checked if all required libraries were available by looking at the list of installed packages:

 ```sh

 $ pip3 list

 ```

After everything was ready, we ran the python file:

```sh

$ python3 mnist_convnet.py

```

Because the code initiates the training of a neural network model, the process took some time to complete but completed successfully in the end.

### Versions and Dependencies

To see the python version which is used to run the code we used the command:

```sh

$ python3 --version

```

The versions of the three libraries tensorflow, keras and numpy are depicted in the same list as mentioned above. To see the dependencies of each library we used the command:

```sh

$ pip3 show <library>

```

When we used this command for the keras and numpy library, we saw that both libraries, are required by tensorflow but do not require furher packages. Tensorflow itself requires several packages which are installed right away when tensorflow itself is installed.

The library versions depend on the system. When we ran the same code on a windows computer with an anaconda distribution and python version 3.7.11, we saw differences in the library versions. However, as long as a python versions 3.6 - 3.9 are used and pip versions >= 19.0, tensorflow can be installed normally and allowing everybody to run the code from the terminal.


## Task 5: What the code does

The ``` $ mnist_convnet.py ``` code, in order to be understood correctly and run smoothly, should be divided into several parts, with each one being run and explained before moving on to the next one.

First, one should start with importing the necessary packages, i.e. ``` numpy ```, ``` tensorflow ``` and ``` keras ```, the latter being imported directly from ``` tensorflow ```. The Tensorflow library here is the most important for the code to run, as it used here for the CNN, i.e. Convolutional Neural Network. Keras comes second in importance, being applied to create the neural network in the last part of the code.

```

$ import numpy as np
$ from tensorflow import keras
$ from tensorflow.keras import layers

```

Having completed the initial preparatory steps, one may turn directly to the code. As this code is designed to recognize the handwritten digits, normalized and centered in a fixed-size 28*28-pixel image, the model and data paramaters must be processed.

```

$ num_classes = 10
$ input_shape = (28, 28, 1)

```

The next part is where one would be to normalize the data, i.e. the pixel values between 0 and 255 to a range between 0 to 1. To make sure this command has been executed correctly, one must use the ``` print() ``` command to check for x_train shape.

```

$ (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

$ x_train = x_train.astype("float32") / 255
$ x_test = x_test.astype("float32") / 255
$ x_train = np.expand_dims(x_train, -1)
$ x_test = np.expand_dims(x_test, -1)

$ print("x_train shape:", x_train.shape)
$ print(x_train.shape[0], "train samples")
$ print(x_test.shape[0], "test samples")

```


Running this set of commands would produce a set of class vectors, which must then be converted into binary class matrices, i.e. transforming numbers into categorical values by using the following code:

```

$ y_train = keras.utils.to_categorical(y_train, num_classes)
$ y_test = keras.utils.to_categorical(y_test, num_classes)

```

Next, building the sequential model would be the most important and complex step of the code. To do that, one would require 7 layers in the line of code, including the convolution layer Conv2D, pooling layer MaxPooling2D, Dropout layer, vector-flattening layer Flatten, and lastly, the output layer dense with softmax activation. To check if the model has been created successfully and correctly and also to get a general understanding of the main outcomes, one might want to run the ``` $ model.summary() ``` command.

The model at issue is sequential, with the outcome being reported tabularly with 3 columns, those being being named layer (type), output shape, and param #. The number of total params and those that have been found to be trainable equals in both cases 34,826, thus allowing to conclude that all paramaters are valid for training.

```

$ model = keras.Sequential(
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

```

The penultimate step would be to train the newly created model. However, one must firstly complete some basic processing of the data for CNN: here one should define the batch size and the number of epochs the neural network will run. In this case, the algorithms will have to reevaluate the model by passing the dataset in both directions 15 epochs (read: times), and 422 times per epoch.

```

$ batch_size = 128
$ epochs = 15

```

Having done that, it is now time to compile and finally train the model. In the given of code, one is to work with categorical crossentropy loss and Adam optimizer.

```

$ model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

$ model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

```

The process will take some time to be completed, but after the machine is done running these lines of code, one should print the results and check for the test loss and test accuracy scores, if one wants to know how well the given model performs.

```


$ score = model.evaluate(x_test, y_test, verbose=0)
$ print("Test loss:", score[0])
$ print("Test accuracy:", score[1])

```
