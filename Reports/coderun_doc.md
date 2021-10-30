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
