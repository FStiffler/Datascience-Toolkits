# Report: Milestone 1

## General Remarks

In Milestone 2 we forgot to add the sha256 hash digest for the packages which is why we added them in milestone 3. For that purpose we had to install the package hashin with `pip install hashin`. After that we could simply use a command on all the requirements to obtain the hash digest:

```sh
$ hashin numpy==1.19.5
$ hashin keras==2.6.0
$ hashin tensorflow==2.6.0
$ hashin matplotlib==3.4.3
```

However we realized that we have several hashes for the same package. Therefore we deleted the environment to install the packages once more and add the hashes. After we have installed the packages with `pip install -r requirements.txt`, we ran the commands listed above once again. Now our *requirements.txt* file was again extended with several hash digests. We accepted our faith and added all the hashes to the table under *Requirements* in the *README.md* file. However, we deleted them again from the requirements file for more reader friendly experience. 
