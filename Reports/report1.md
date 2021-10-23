# Report: Milestone 1

## Task 1: Data

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
