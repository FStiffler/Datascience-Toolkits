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

In mileston 1 we described which packages are actually necessary to run the [mnist_convnet.py](mnist_convnet.py) file. Based on these dependencies we were able to create a [requirements.txt](../requirements.txt) file in the Github root folder. To create the file we made sure to set our locally directory to the root folder and then we used the Linux command:

```sh

$ touch requirements.txt

```

This created a empty text file. To retrieve the relevant information about the dependencies, we activated our old python environments (when there were any already) and called `pip list`. Because we installed all required libraries already in milestone 1 and successfully ran the code with said libraries and library versions we could simply copy the names and versions. The two values were pasted into the *requirements.txt* file. Each line contains one required library and the according version separated by *==*. These libraries are not yet installed in our new environment which is why we deactivated the old environment and reactivated the new environment we just created previously (again make sure to set the correct working directory). Based on this requirements file we could now install all the needed packages also into the new environment by running:

```

pip install -r requirements.txt

```

The packages were installed smoothly. And because they were now available in the new environment, we could simply run the python file with `python3 mnist_convnet.py`. No errors were raised. The required packages were also added to the README file in the root folder under the section *Requirements*.
