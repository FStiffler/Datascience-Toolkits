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


## Task 1: Docker Compose

**1. Install docker composer**

We followed the instructions of this [link](https://docs.docker.com/compose/gettingstarted/) to introduce docker-compose already in Task 6 of the [milestone 2](report2.md). However, we decided to redo it after we had troubles to get our container up and running in the last milestone. Furthermore, we have had already deleted the docker-compose file due to the mentioned troubles. So this was our chance to a fresh start.

- *Install docker compose*
Since I (Flurin) had not yet installed docker-compose on his machine, I had to do this first.

```sh
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose

```

- *Testing docker compose*
After that both of us were again on the same level and we were able to follow the introduction in the link. We are not going to explain everything again. But we were able to successfully complete the tutorial and found it really helpful to understand docker compose.

**2. What services are being used in the example yml file?**

In our [last report](report2.md) we also already shortly discussed the two services used by the application, namely `web` and `flask`.  The former binds a container created from an image defined in a Dockerfile to a exposed port. The later uses a public Redis image for the Docker Hub. On [redis.io](redis.io) the following description is offered:

*Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker. Redis provides data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes, and streams.*

Both services relate to the host names with the according host and port settings defined in the docker-compose and app file.

**3. What ports are being used?**

Within the application, port 6379 is used for Redis. For the web service, our host machine and the container are both bound to the port 5000. The two running containers are depicted in the following tables:


Name | Command | State | Ports               
--|---|---|--
composetest_redis_1 |  docker-entrypoint.sh redis ... | Up    |  6379/tcp                                
composetest_web_1   |  flask run         |               Up   |   0.0.0.0:5000->5000/tcp,:::5000->5000/tcp
