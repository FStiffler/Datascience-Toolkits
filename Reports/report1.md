# Report: Milestone 1

## Task 1: Data

The provided MNIST dataset is a subset of a large NIST database, containing handwritten digits and divided into 4 separate files with both images and labels sets:
a training set of 60,000 examples and a test set of 10,000 examples.


The database was formed from two Special Databases (NIST's 3 and 1), with the former reported to be much cleaner due to the difference in study subjects' differences.
Merging the databases into a single one was crucial for drawing valid conclusions from the learning experiments conducted,
 while also having two independent sets of samples - i.e. training and test sets.


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

However, we recognized that we simply downloaded the source code of the Github page with this linux command. To actually download the python file with actual code python code, we had to click on *Raw* on the Github page and copy the URL of the new window. After that we could rerun the command above with the now correct URL.

The python file was stored in the local root folder of the our repository as *mnist_convnet.py*. The file was only stored to the root folder of the previously created *Milestone1* branch. The *master* branch stayed unaffected. The next step was to commit and push the file to the same branch on the remote repo on Github.

## Task 3: Commit

The downloaded file has staged first before we can commit it:

```sh

$ git add mnist_convnet.py

```

Then the file can be committed to our local repository with the command:

```sh

$ git commit -m <commit_message>

```

Finally, the file is pushed to the remote repo on Github:

```sh

$ git push

```

## Task 4: Run code

### Task 4.1: Necessary steps to run the code

To run the code, first we had to activate our virtual python environment (if a virtual environment was set up for this project). To activate the environment with have to use the following command:

```sh

$ source <env_name>/bin/activate

```

When the python evironment is active, we can start installing libraries required for the project (In this case, required to run the *mnist_convnet.py* file) into this environment. If we do not do that, the file will not run due to missing dependencies. To install libraries we need pip allowing us to access python libraries from the python package index (PyPI). If pip is not already installed, we can do so with the following linux command:

```sh

$ sudo apt-get install -y python3-pip

```

We can verify the installation:

```sh

$ pip3 --version

```

If pip is already installed but we want to make sure that it is the latest version we can use the command:

```sh

$ pip3 install --upgrade pip

```

Now with pip available, we can install the required libraries:

```sh

$ pip3 install tensorflow

```
 In the file three libaries are imported, namely *tensorflow*, *keras* and *numpy*. The library tensorflow also contains the keras API which is why, a separate installation of keras is not necessary. The numpy library comes with the tensorflow distribution as well. We can check if all required libraries are available by looking at the list of installed packages:

 ```sh

 $ pip3 list

 ```

Now that everything is ready, we can run the file:

```sh

$ python3 mnist_convnet.py

```

Because the code initiates the training of a neural network model, the process takes some time to complete.

### Task 4.2: Versions and Dependencies

To see the python version which is used to run the code we can use the command:

```sh

$ python3 --version

```

The versions of the three libraries tensorflow, keras and numpy are depicted in the list already called before. To see the dependencies of each library we can use the command:

```sh

$ pip3 show <library>

```

If we use this command for the keras and numpy library, we see that both libraries, are required by tensorflow but do not require furher packages. Tensorflow itself requires several packages which are installed right away when tensorflow itself is installed.

The library versions depend on the system. When we ran the same code on a windows computer with an anaconda distribution and python version 3.7.11, we saw differences in the library versions. However, as long as a python versions 3.6 - 3.9 are used and pip versions >= 19.0, tensorflow can be installed normally and we can run the file from the terminal. 
