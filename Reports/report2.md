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


## Task 5

That is something, we did not actually do before milestone 2. Therefore we created a [requirements.txt](../requirements.txt) file in the Github root folder. To create the file we made sure to set our locally directory to the root folder and then we used the Linux command:

```sh

$ touch requirements.txt

```

This created a empty text file. To retrieve the relevant information about the dependencies, we activated our python environments and called `pip list`. Because we installed all required libraries already in milestone 1 and successfully ran the code with said libraries and library versions we could simply copy the names and versions. The two values were pasted into the *requirements.txt* file. Each line contains one required library and the according version separated by *==*. Based on this requirements file everybody can install the necessary libraries to run the code:

```

pip install -r requirements.txt

```
