# Lab 1: Docker for Databases

In this laboratory we will run multiple containers using Docker Compose. We will have
3 containers: 

* PostgreSQL: Preloaded with movies information
* MySQL: Preloaded with movies information
* Python Web App 

[Lab 1 Diagram](documentation_images/lab1_diagram.png)

### Prerequisites
* [Install docker](https://docs.docker.com/engine/install/) 
* Install a db client (i.e. [DBeaver](https://dbeaver.io/download/)) 
* Install docker compose (only if you are on Linux)

> NOTE: On desktop systems, such as Docker Desktop for Mac and Windows, docker compose is already included. 
> No additional steps are needed. 

### What You Will Learn
You'll learn how to:
* Read a docker-compose.yml file 
* Mount volumes and how data is persisted through them 
* Create multiple databases in a docker container leveraging a docker-compose.yml file 
* Connect to different databases running inside the container using a db client
* Connect to different databases running inside the container using the command line

 
## Let's get started

### Docker Compose
In this folder there's a pre-defined [`docker-compose.yml`](docker-compose.yml) file, let's walk through the file
to make sure you understand it. 

There are multiple clauses and keywords within this file: 

```dockerfile
version: "3"
services:
    postgres:
        container_name: postgres_db
        image: postgres:14-alpine
        ports:
            - "32001:5432"
        environment:
            - "POSTGRES_PASSWORD=${POSTGRES_PASSWORD}"
        volumes:
            - "./databases/postgres_movies_database.sql:/docker-entrypoint-initdb.d/movies_database.sql"
    mysql:
        container_name: mysql_db
        image: mysql:8.0
        platform: linux/amd64
        ports:
            - "32002:3306"
        environment:
            - "MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}"
        volumes:
            - "./databases/mysql_movies_database.sql:/docker-entrypoint-initdb.d/movies_database.sql"
    webapp:
        container_name: webapp
        build: ./app
        ports:
            - "5000:5000"
        depends_on:
          - postgres
          - mysql
        environment:
            - "MYSQL_URI=${MYSQL_URI}"
            - "POSTGRES_URI=${POSTGRES_URI}"
```

* `version`: This specifies the version of docker compose, in this case we are using version 3, and Docker will provide the appropriate features for this version. 
* `services`: This section defines all the containers that can be created. Each service represents a container that will have its own name and configuration.
    * In this definition we have 3 services `mysql`, `postgres` and `webapp`, this last one is build from [this Dockerfile](app/Dockerfile) definition and will only be used
    for displaying results.  
* `container_name`: specifies a custom container name, rather than a generated default name.
* `image`: Is used to mention the image name from which container will spin-up from. Image can be in the local system or hosted on some remote repository. 
* `ports`: This is used to map the container’s ports to the host machine `host port 32001: container port 5432`.
* `environment`: Defines the environment variables set in the container.
* `depends_on`: Express dependency between services. In this case `postgres` and `mysql` service are started before `webapp`.
* `volume`: File system mounted on docker container. In this case we are using a `bind mount` to copy the [databases/postgres_movies_database.sql](databases/postgres_movies_database.sql) file into
the postgres database and [databases/mysql_movies_database.sql](databases/mysql_movies_database.sql) into the mysql database when the container starts.


> NOTES: 
> **Why do we need port mapping?** 
>
> As a general rule, a port can only map to a single service or process on each host. 
> Imagine that you have multiple PostgreSQL containers on a single host. By default, 
> each PostgreSQL instance wants to bind to port 5432 as it is its default port, while you could manually modify each 
> container to bind the container's service to a unique host port, this quickly becomes a hassle at scale.
> Instead, Docker and other container managers make it easy to map ports between the host OS and the container


### Environment variables in compose 
If you have multiple environment variables, you can substitute them by adding them to a default environment variable file named 
`.env` which compose automatically looks for in the project directory, alternatively you can provide a path to your environment 
variables file using the `--env-file` command line option. 
 
For this lab, we have a [`.env`](.env) file defined within this directory. Each line in an `env` file must be in `VARIABLE=VALUE` format. 
Compose files use a Bash-like syntax `${VARIABLE}` to evaluate. 

**.env** file: 

```shell script
POSTGRES_PASSWORD=secret1
```

**docker-compose.yml** file: 

```shell script
"POSTGRES_PASSWORD=${POSTGRES_PASSWORD}"
```

### Docker Compose commands

`docker compose up`: This command does the work of the `docker-compose build` and `docker-compose run` commands. 
It builds the images if they are not located locally and starts the containers.

`docker compose down`: This command is used to destroy all the containers/services run from the Docker Compose file.

### Running docker compose 

Now that we are all set, let's run our docker compose file: 

> NOTE: Make sure you run this commands within the directory that
> contains the `docker-compose.yml` file (in this case within `Lab1_DockerForDatabases` folder)

```shell script
$ docker compose up
```

Open another terminal window and make sure your container is running: 

```shell script
$ docker compose ps
NAME                COMMAND                  SERVICE             STATUS              PORTS
mysql_db            "docker-entrypoint.s…"   mysql               running             33060/tcp, 0.0.0.0:32002->3306/tcp
postgres_db         "docker-entrypoint.s…"   postgres            running             0.0.0.0:32001->5432/tcp
webapp              "python server.py"       webapp              running             0.0.0.0:5000->5000/tcp
```

### Explore the webapp

Now that we have our containers running, if you go to [`http://localhost:5000/`](http://localhost:5000/) you should have something like the 
following image: 

[Wep app](documentation_images/webapp.png)

In here, we can see two sections, both are lists of movies with their ratings but one is loaded in MySQL database and the other one in PostgreSQL database. 

### Connect to the PostgreSQL database
Now that our container is running, we will connect to the PostgreSQL instance.

#### Using the CLI

The following command lets you connect to the PostgreSQL CLI running inside the Docker container, we will need the name of 
the **service** we want to connect to.

```
$ docker compose exec postgres bash
bash-5.1# 
```

Once the interactive terminal is started, you can connect to the PostgreSQL instance using the default user.

```
bash-5.1# psql -h localhost -U postgres
psql (14.5)
Type "help" for help.

postgres=# 
```

* `-h`: You need to provide the hostname on which the PostgreSQL Docker container is running. 
* `-u`: By default, the PostgreSQL image uses a username **postgres** that you can use to log in to the database.


You can now run SQL queries against this database! 

### ✏️ Exercise 1: Connect to the MySQL instance using the CLI 
Connect through the CLI to the MySQL instance

### ✏️ Exercise 2: Connect to the MySQL instance using the db client of your preference
Now that you know how to connect using the CLI, try to do the same with the db client, remember to use the password that 
was set in the `.env` file. 

### ✏️ Exercise 3: Connect to the PostgreSQL instance using the db client of your preference
Now that you know how to connect using the CLI, try to do the same with the db client, remember to use the password that 
was set in the `.env` file. 

### ✏️ Exercise 4: Insert some data into the databases: 
Since we haven't seen DML statements, I'll give you the statements you will need to run, you may replace the names and ratings with your
favorite or least favorite movies: 

On MySQL:
```
INSERT INTO movie VALUES ("Harry Potter and the Goblet of Fire", 10.0);
```

On PostgreSQL:
```
INSERT INTO movie VALUES ('Twilight', 0.4);
```

**Questions**:

* What happens in the UI when you refresh the page? 

### ✏️ Exercise 5: Restart your containers
Using the commands to stop and run Docker Compose, do it again to restart our containers. 

**Questions**:

* What happened to the data you inserted in Exercise 4? 
* Why does it happen? 

### ✏️ Extra for nerds: Mount a volume for persisting the new data
So now that you know why the newly inserted data is not available, you can redefine your `docker-compose.yml` file
to persist the data inserted in Exercise 4. 

### Stop your services! 
Don't forget to stop your containers when you are done.

### Troubleshooting: 
These are some of the most common errors that you can encounter, if you have and issue and feel like it should be added 
to the list please share with the teacher(s).

#### Error: Public Key Retrieval
If you have this error with mysql, go to the driver properties and change the `allowPublickKeyRetrieval` to **true**.

[Error: Mysql](documentation_images/error_mysql.png)


