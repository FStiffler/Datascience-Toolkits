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


### Task 5: What the code does

Dependencies that must be imported before running the could could be checked for by running the following command:

```

$ pip show keras
$ pip show tensorflow

```

By checking for pre-required dependencies, one finds that keras package runs on version 2.6.0, and itself is required by the tensorflow package, despite having no additional requirements of its own.

Tensorflow package, on the other hand, also runs on 2.6.0 version, and is an open source machine learning framework for everyone, and has a rather wide list of required pre-installed packages to run:



| wrapt                | 1.12.1  | _
| gast                 | 0.4.0   | _
| astunparse           | 1.6.3   | _
| h5py                 | 3.1.0   | _
| numpy                | 1.19.5  | _
| protobuf             | 3.19.1  | _
| flatbuffers          | 1.12    | _
| opt-einsum           | 3.3.0   | _
| tensorflow-estimator | 2.6.0   | _
| typing-extensions    | 3.7.4.3 | _
| tensorboard          | 2.7.0   | _
| keras-preprocessing  | 1.1.2   | _
| six                  | 1.15.0  | _
| google-pasta         | 0.2.0   | _
| wheel                | 0.36.2  | _
| clang                | 5.0     | _
| absl-py              | 0.15.0  | _
| grpcio               | 1.41.1  | _
| keras                | 2.6.0   | _
| termcolor            | 1.1.0   | _





The indicated versions of each of these required packages could be checked by running the command

```

$ pip3 list

```

which produces the complete list of packages and their respective versions that go together with tensorflow and/or keras.

Having run the code command, one receives a message about automatic dowloading of data from both tensorflow and keras storagespaces in googleapis. The technical details of the training process are also displayed, e.g. the X train shape (60000, 28, 28, 1), where 60,000 stands for the 60 thousand training samples, and double 28 represents the 28*28 field in which images are centered. Tensorflow also specifies that the code is being run with tensorflow binary, which was optimized with Deep Neural Network Library.

The model at issue is sequential, with the outcome being reported tabularly with 3 columns, those being being named layer (type), output shape, and param #. The number of total params and those that have been found to be trainable equals in both cases 34,826, thus allowing to conclude that all paramaters are valid for training.

There were reported 15 epochs, with each following a rapid downward trend of loss numbers, while showing a general (although with insignificant exceptions) upward trend in both accuracy and val_accuracy figures. To be more precise, the first epoch reported 0.3812 loss, while the last 15th epoch showed only 0.0324. As to the accuracy numbers, the val_accuracy figures were set equal to 0.9783, differentiating by almost 0.02 point from the 0.9918 in the 15th epoch. Overall, the test loss numbers were rounded up at 0.0255, and the test accuracy figures showed 0.9919.
