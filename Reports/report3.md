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

**Addendum**

We asked why so many hashes are generated in the lecture. Arthur informed us that, first of all we can simply look up the hashes for a package on PyPI when going on package site, selecting *download files* and then click *view* (And we spend so much time to find out how to generate those exact hashes) and second of all, we were also informed that packages come with different wheels optimized for the computer architecture the package is running on. We generated one hash for every wheel which is why we have that many hashes. We decided to keep all the hashes already created (since we do not actually know which wheel is used and Arthur told us it is not that important). For additional packages we are going to add wheels as well.


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

**4. How does the host machine (e.g. your computer) communicate with the application inside the Docker container. Which ports are exposed from the application to the host machine?**

In the docker file we can see that the port 5000 is exposed from the container. This port is mapped to port 5000 of our local machine in the docker-compose file. Therefore our local machine with the local host IP 127.0.0.1 can communicate with the docker container over the port mapping 5000:5000.

**5. What is localhost, why is it useful in the domain of web applications?**

The "localhost" is the standard name provided to the address of the local computer in a computer network. It is therefore comparable to a domain (i.e google.com) which used to connect to a server with a particular IP address. In the case of "localhost" we connect to our own computer with the default loopback address 127.0.0.1. The localhost domain has several perks:

- It allows to perform connection tests by sending ping requests.
- It allows developers to test web applications on their local systems first before deploying them on a server exposed to the internet.
- It allows to block websites from being accessed.

## Task 2: PostgreSQL

### What is PostgreSQL? Is it SQL or NoSQL?

PostgreSQL is a open source object-relational database management system (RDBMS). It is a tool to create, define and transform databases. It applies the SQL-Standard. SQL stands for **S**tructred **Q**uery **L**anguage and is a programming language designed to work with databases. It consists of Data Query Language to make data queries on an existing database, Data Manipulation Language to manipulate the data in a database, Data Definition Language to define data bases and their schemes and Data Control Language to manage access rights to a database.

**SQL database:**

An SQL database is a relational data base where the entries are connected with each other other so called relations. It allows easy queries to connect related data and receive data insights.

**NoSQL:**

NoSQL databases are not relational. They find different ways to store data like for example Key-Value store, Column store, Document store or Graph store. This allows for higher scalability and work with large amount of data.

**Is PostgreSQL now SQL or NoSQL?**

PostgreSQL is a relational database management system in a classical sense. However it has also features to store JSON files which is normally found in NoSQL databases. But since we can only interact with PostgreSQL with SQL, we can't really call it a NoSQL system.

### Run a PostgreSQL Server via Dockerfile

#### Make it running

We did not want to do this task in our current project, so we created new directory `/home/user/Documents/jokes`. After that, the first thing we had to do was to pull the official PostgreSQL image from Docker Hub corresponding to Version 14:0. We looked up the images and the required command for this task [here](https://hub.docker.com/_/postgres):

```sh
$ docker pull postgres:14
```

In a next step we wanted to build a container from the image with a name and a password. We used the command from the mentioned website:

```sh
$ docker run --name postgres -e POSTGRES_PASSWORD=123 -d postgres:14
```

We checked if our container was running with `docker ps`. The container was now running but we were not yet able to interact with it. Therefore we stopped the container again and started to create a yml file which would grant interaction with a SQL database instance. We followed the instructions on this [websites](https://towardsdatascience.com/how-to-run-postgresql-and-pgadmin-using-docker-3a6a8ae918b5) to obtain a running instance of postgres with pgAdmin. We modified the file a bit to adjust it for our needs however.

```
version: '3.8'
services:
  db:
    container_name: pg_container
    image: postgres:14
    restart: always
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: 1234
      POSTGRES_DB: test_db
    ports:
      - "5432:5432"
  pgadmin:
    container_name: pgadmin4_container
    image: dpage/pgadmin4
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: 1234
    ports:
      - "5050:80"
```

This docker-compose file composes two containers. The db container which runs on an image of postgres and thus runs PostgreSQL in the container and the pgAdmin container which runs on an image of pgAdmin4. In the db container we defined environment variables such as the user, the password and the database to work on. Furthermore we defined over which ports we want to access the database server. The database server exposes the port 5432 which is mapped to the same port to our local machine. In the pgAdmin container we had to define a user email and a password as well. We mapped the port 5000 of our local machine to the port 80 of the docker container. Finally we ran `docker-compose up` to create the a running instance of the images. Since pgAdmin is a webbased client we were now able access it over our localhost and the defined port `localhost:5050`. We entered the email address and password defined in the docker-compose file and had now access to pgAdmin. Since we did not yet add a database server to our running instance of pgAdmin, we had to do that according to the description on the [websites](https://towardsdatascience.com/how-to-run-postgresql-and-pgadmin-using-docker-3a6a8ae918b5). We named the server *jokes_server*. After that we had to follow the instructions to find out the IP address on which the database server was running. So we looked at the containers with `docker ps`:

CONTAINER ID | IMAGE | COMMAND | CREATED | STATUS | PORTS | NAMES
... | ... | ... | ... | ... | ... | ...
51c3e0a71646 |  postgres:14   |   "docker-entrypoint.s…"  | 20 minutes ago  | Up 5 minutes  |  0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   |  pg_container
3f561c1d0bb7 |  dpage/pgadmin4 |  "/entrypoint.sh"  |    20 minutes ago  |  Up 5 minutes  |  443/tcp, 0.0.0.0:5050->80/tcp, :::5050->80/tcp  | pgadmin4_container

We saw on which ports the containers are running but not on which IP address. Therefore we had to dig deeper with `docker inspect pg_container | grep IPAddress`. From that information we saw that the container was running on the IP `172.18.0.2` We added this information to the host information and saved everything. Now we had a connection to the server and were also able to see our already created test database called *test_db*. An even easier way to connect to the postgres server would be to add the name of the container to the host name.

#### Docker volumes

To see what happens to stored data in our database we created a table and inserted data into it via SQL script. After that we stopped and removed our docker containers with `docker-compose down`. Then we created new containers again with `docker-compose up`. We saw, that we had to reconnect to the postgres server from scratch and that our table with data was gone. Based on this information we knew, that we had to mount volumes to our container which would store the data of the container even when we remove them. Therefore we further adjusted the yml file based on information obtained on [DockerHub](https://hub.docker.com/_/postgres) and on the [website of pgAdmin](https://www.pgadmin.org/docs/pgadmin4/development/container_deployment.html):
```
version: '3.8'
services:
  db:
    container_name: pg_container
    image: postgres:14
    restart: always
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: 1234
      POSTGRES_DB: test_db
      PGDATA: /var/lib/postgresql/data
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin4_container
    image: dpage/pgadmin4
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: 1234
    ports:
      - "5050:80"
    volumes:
      - pgadmin_data:/var/lib/pgadmin    
```

When we ran this we got an error message:

```
ERROR: Named volume "db_data:/var/lib/postgresql/data:rw" is used in service "db" but no declaration was found in the volumes section.
```

Upon some internet research it became clear that we have to define the volumes to use in a separate volumes section. And since we have no volumes yet, we have to create them first. A way to do both in the same yml file is depicted in the following code:

```
version: '3.8'
services:
  db:
    container_name: pg_container
    image: postgres:14
    restart: always
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: 1234
      POSTGRES_DB: test_db
      PGDATA: /var/lib/postgresql/data
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin4_container
    image: dpage/pgadmin4
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: 1234
    ports:
      - "5050:80"
    volumes:
      - pgadmin_data:/var/lib/pgadmin   

volumes:
  postgres_data:
  pgadmin_data:
```

This code creates two docker volumes which store all the data of pgAdmin and postgres locally and thus should store changes we make to our database. We tried it out by rerunning the the docker-compose file and adding data to our database. Then we removed the containers and created them again. This time everything was still there. On the pgAdmin page we could reconnect to our defined postgres server and in the server we were able to make a query on our database to receive the previously introduced data.

#### Python script to store joke in DB

Since we work in another project folder and we didn't want to pollute our project python environment, we created a new python environment in the `jokes` directory called *jokes* as well and activated that. After that we searched for a python package to communicate with our SQL database. We stumbled upon this [website](https://www.postgresqltutorial.com/postgresql-python/connect/) when we searched for solutions. The package used is `psycopg2`. When we tried to install the package with `pip install psycopg2`, however, we got a ton of error messages. Therefore, we searched for solutions and found an easy fix by just installing the standalone binary package `psycopg2-binary`. Now we had to create a python file to interact with our database server. First we tried to just create the database.

```
# Import package
import psycopg2

# Establish connection to sql server
con = psycopg2.connect(
    host="172.18.0.2",
    port="5432",
    database="test_db",
    user="admin",
    password="1234")

# Creat cursor
cur = con.cursor()

# Create new database 'ms3_jokes'
sql = '''CREATE DATABASE ms3_jokes''';
cur.execute(sql)

```
When we ran the file with `python3 jokes.py`, we got an error message saying `psycopg2.errors.ActiveSqlTransaction: CREATE DATABASE cannot run inside a transaction block`. The problem seems to be that psycopg2 automatically starts a transaction when connecting to a database. We have to turn that off and allow autocommit with `<connection_name>.autocommit = True`. After we adjusted our python script with this line of code we were able to see the newly created database in pgAdmin. The next step was to create a table. We added the according command to python. But when we ran the file once again we saw that the table was created in our *test_db* defined in the docker compose file. So we figured that we had to close the connection to this database after we have created the new database *ms3_jokes* and establish a new connection. The last step was to insert a joke into our table and querie it again to print it to the console. With this final code everything worked perfectly:

```
# Import package
import psycopg2

# Establish connection to test_db
con = psycopg2.connect(
    host="172.18.0.2",
    port="5432",
    database="test_db",
    user="admin",
    password="1234")

# Turn off transaction mode and enable autocommit
con.autocommit = True

# Creat cursor
cur = con.cursor()

# Create new database 'ms3_jokes'
cur.execute('CREATE DATABASE ms3_jokes')

# Close connection
con.close()

# Create connection with new database
# Establish connection to test_db
con = psycopg2.connect(
    host="172.18.0.2",
    port="5432",
    database="ms3_jokes",
    user="admin",
    password="1234")

# Turn off transaction mode and enable autocommit
con.autocommit = True

# Creat cursor
cur = con.cursor()

# Create a new table
cur.execute('''CREATE TABLE jokes (
    ID int PRIMARY KEY
        GENERATED ALWAYS AS IDENTITY,
    JOKE text
    )''')

# Insert joke
cur.execute('''INSERT INTO jokes (JOKE) VALUES (
    'When I wrote this code, only me and God knew how it works. Now only God knows...'
    )''')

# Selet joke
cur.execute('SELECT * FROM jokes')

# Print jokes
jokes = cur.fetchall()
for row in jokes:
        print("Id = ", row[0], )
        print("Joke = ", row[1])

# Close connection
con.close()
```

#### Is the joke still there?

The last task was to check if our joke is still there after we removed the containers with `docker-compose down` and recreate them with `docker-compose up`. Theoretically it should work since we have done it before without the python script. Luckily our expectations were met. The joke was still there after recreating the containers. Task 2 check!


## Task 3: Storing images to relational databases

### How do you need to represent/transform image data to save it to a relational database?

To answer this question we searched the web for answers and came across a [webpage](https://howtodiscuss.com/t/store-image-in-postgres/79153) on which it is explained how to insert images into a PostgreSQL database and another [webpage](https://www.futurelearn.com/info/courses/programming-103-data/0/steps/64743) explaining how the raw data of images is stored on a computer. It appears that images are binary data consisting of raw bytes which is not human readable. This is why they can be stored as BLOB data type or in case of PostgreSQL as BYTEA data type in a relational database. Both data types represent binary data and allow storage of binary strings. However, storing images as BLOBs or BYTEAs is not recommended.

Another way to store images in a database (though indirectly) is by storing the file path to the picture in the file system in the database. Meta information about the pictures is provided in additional database table columns.

### Look at your own dataset

**1. How is your data structured?**

When the mnist data is loaded in [data_prepared.py](../original/mnist_convnet.py), the pictures are represented as numpy array with shape (70000, 28, 28). So we have a total of 70000 pictures in the training and test set with 28 times 28 pixels. In order to be used with the Keras API we have to transform the array to the form (70000, 28, 28, 1). But how do we have to reshape the data in order to insert it into a relational database?

**2. Explain how you would define your relational database tables in terms of their attributes to save your data. What kind of data types could you us?**

Obviously we will have to work with some sort of array data type and not with binary data type as described before. We looked at the provided [link](https://www.postgresql.org/docs/12/datatype.html) and saw, that an array data type exists. But after hours of research about how we now can insert our numpy arrays into a database as array as well, we realized that there is no way to do it. However, we found out that we can convert our numpy array to bytes and back using the package `pickle`. We find a instruction on how to do it [here](https://stackoverflow.com/questions/60278766/best-way-to-insert-python-numpy-array-into-postgresql-database). So we tried it out with one picture of our mnist dataset.

```
# Import package
import pickle

# Select test example
test = x_train[1]

# Return the array as byte stream
test_bytes = pickle.dumps(test)

# Transform back to original array
test_back = pickle.loads(test_bytes)

```
This worked perfectly. So we knew we can load data, transform it to a byte stream, read it into a database as datatype bytea and reload it. As for the structure of our database, we thought about creating one single table with all the data. This would require us to add at least a column of type boolean for training. If a value in this column is `true` or `1`, we know that the observations belongs to the training data. When it is `false` or `0`, we know that the observation must be from the test data. Another column of data type int would be used to store the picture labels (actual handwritten digit in picture). So our table, for example, could look like this:

ID | Picture | Training | Label
... | ... | ... | ...
1 | <byte_stream> | 1 | 3

**3. What additional relational database table attributes might make sense to easily query your data?**

We could think of horizontal partitioning so that we can store our data the same way as we load it into python (x_training, y_training, x_test, y_test). But then we would have to create and query four different tables. That is quite unhandy. As for additional attributes, we could maybe add additional meta data to the pictures but since we are not given any, this is not an option.

### Repeat Task 2 for own dataset

To repeat task 2 but now with our own data we created a new directory `m3t3` in our project directory this time. We copied the docker compose and python file from task 2 into this directory because we decided to build upon this code.

**First Step**

The first step was to adjust the docker compose file. We added new volumes since the volumes initially created for task 2 might be still used if we wanted to compare something. Furthermore, we renamed the database to be initialized:

```
version: '3.8'
services:
  db:
    container_name: pg_container
    image: postgres:14
    restart: always
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: 1234
      POSTGRES_DB: task3
      PGDATA: /var/lib/postgresql/data
    ports:
      - "5432:5432"
    volumes:
      - postgres_dataT3:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin4_container
    image: dpage/pgadmin4
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: 1234
    ports:
      - "5050:80"
    volumes:
      - pgadmin_dataT3:/var/lib/pgadmin

volumes:
  postgres_dataT3:
  pgadmin_dataT3:
```
After that we ran `docker-compose up`, opened a browser, logged into pgAdmin, added the SQL Server and checked if the *task3* database is there already. Everything was fine.

**Second Step**

The next step was to prepare the python file. Before we could prepare the file, however, we had to activate our personal environments for the project and install the psycopg2 package just like we did for Task 2. After that we created a python file with the following abilities:

 *1. Load mnist data*

Here we could simply use the module [load_data.py](../code/load_data.py) created in milestone 2 already.

 *2. Take one picture as sample*

We took the first picture

 *3. Show picture*

Here we used the `Pillow` package as indicated in the Milestone description. Because `Pillow` is already integrated in matplotlib which we have already installed, no further installation process is required. We can import the required functionality to show the picture with `from PIL import Image`

 *4. Transform picture to byte stream*

For this ability the package `pickle` has to be installed. This is a standard library and thus does not need to be installed specifically.

 *5. Create table to insert transformed sample picture into*

We had to connect to the database first and then we were able to create a new table.

 *6. Insert sample picture into table*

 Here we had some troubles at first. We used the following code:

 ```
 cur.execute(
    """
    INSERT INTO pictures (Picture)
    VALUES (%s)
    """,
    (sample_bytes)
)

 ```
Since our SQL Table contains a ID which auto increments, we only have to define the bytea value to be inserted. One problem though. We always got an error and we couldn't figure out what the problem was for a long time just to remember that a tuple with one value needs a comma nevertheless. So we fixed it.

```
cur.execute(
   """
   INSERT INTO pictures (Picture)
   VALUES (%s)
   """,
   (sample_bytes, )
)

```

 *7. Reload sample picture from database*

Simple SQL statement to query the data.

 *8. Recreate object from byte stream*

Here we had to use `pickle` again to retransform the bytes stream.

 *9. Visualize the picture again to check if the picture transformation has worked*



Now that we had a python file which we tested step by step we wanted to run everything from scratch. So we deleted the table in our database and removed the containers. Then we restarted the containers and ran the file with `python task3.py`. But we were not able to connect to the database. After inspecting the container we realized, that the IP address of the PostgreSQL container has changed and since we defined the IP in the python file directly, the file is no longer able to find the database host. Therefore, we replaced `host=127.30.0.2` with `host=pg_container`. We based this idea on the earlier discovery that we can log into our server by simply defining the name of the host container and not the IP address. Sadly this did not work. So we tried to assign a static IP address to the container. But without luck. After a lot wasted time we searched for a different approach. Finally we found a solution which stated that we simply have to replace the actual IP address in the python file which is used to connect to the database by the string `localhost`. After we changed the file accordingly we were able to connect to our database and run the file successfully. The sample picture was shown before and after it was inserted into the database and it looked the exact same twice.
