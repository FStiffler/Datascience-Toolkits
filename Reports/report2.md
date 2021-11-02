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


## Task 5: Virutal environment and requirements files

### What are virutal environments?

As we mentioned already in our milestone 1 report, some of us already worked in a virtual environments. A virtual environment allows us to work with different dependencies on each project. We might need numpy 1.18.1 for one project but numpy 1.19.1 for another one. In this case virtual environments provide an solution to this problem. We can create two environments with two different versions of numpy and when working on a project, we just activate the one with the correct numpy version.

### How can we set up a virutal environment?

For the purpose of demonstration, we set a new environment from ground and assumed that nothing is preinstalled yet. Therefore, we needed to have pip available before we could even install the virutalenv library which in turn would allow us to install and create virutal environments. For this purpose pip was installed first:

```

sudo apt-get install python3-pip

```

With pip available we could install the virtualenv library:

```

pip install virtualenv

```

Now everything was ready to create a new environment. First of all we had to think of the directory where we wanted to create the virtual environment. It totally makes sense to create the environment within the project directory for which the environment is needed. This, however, implies that we have to prevent git from tracking changes to the virtual environment. Therefore we have to add the environment directory to the gitignore file. For this, please refer to Task 2. For this example we wanted to do exactly that. So we changed our local directory to the project directory and used the following command to create the environment:

```

virtualenv <environment name>

```

The environment is created with the default python version installed on the computer. But we could also define other python versions to use in the environment: as long as we have downloaded and saved them somewhere:

```

virtualenv --python=<Path to python executable to use (for example python3.6)> <Path to location where environment is to be created>

```

Now that the virtual environment was created we could activate it with

```

source <environment name>/bin/activate

```

The virtual environment was now activated and we were able to install libraries.

### How can we make a requirements file work with the virtual environment?

In mileston 1 we described which packages are actually necessary to run the [mnist_convnet.py](mnist_convnet.py) file. Based on these dependencies we were able to create a [requirements.txt](../requirements.txt) file in the Github root folder. To create the file we made sure to set our locally directory to the root folder and then we used the Linux command:

```sh

$ touch requirements.txt

```

This created a empty text file. To retrieve the relevant information about the dependencies, we activated our old python environments (when there were any already) and called `pip list`. Because we installed all required libraries already in milestone 1 and successfully ran the code with said libraries and library versions we could simply copy the names and versions. The two values were pasted into the *requirements.txt* file. Each line contains one required library and the according version separated by *==*. These libraries are not yet installed in our new environment which is why we deactivated the old environment and reactivated the new environment we just created previously (again make sure to set the correct working directory). Based on this requirements file we could now install all the needed packages also into the new environment by running:

```

pip install -r requirements.txt

```

The packages were installed smoothly. And because they were now available in the new environment, we could simply run the python file with `python3 mnist_convnet.py`. No errors were raised. 
