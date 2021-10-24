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
The file is stored in the local root folder of the our repository as **mnist_convnet.py**. The file is only stored to the root folder of the previously created **Milestone1** branch. The **master** branch stays unaffected. The next step is to commit and push the file to the same branch on the remote repo on Github.

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
